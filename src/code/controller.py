import uuid
import sqlite3 as sql
from code.login import Login
from code.register import Register
from code.dataHandler import DataHandler
from code.password import Password

class Controller:
    def __init__(self, connection: sql.Connection):
        super().__init__()
        self.authenticated = False
        self.__connection = connection
        self.__user_name: str = None
        self.__data_handler: DataHandler = None
        

    def login(self, username: str, password: str, remember: bool) -> bool:
        login = Login(self.__connection, username, password, remember)
        
        if not login.authenticated:
            return False
        
        self.__user_name = login.user_name
        self.__data_handler = login.data_handler
        self.authenticated = login.authenticated
        return True
    
    
    def register(self, username: str, email: str, password: str) -> bool:
        register = Register(self.__connection, username, password, email)
        
        if not register.registered:
            return False
        return self.__send_email(email, None)


    def forgot_password(self, username: str) -> bool:
        cursor = self.__connection.cursor()
        cursor.execute(f'''SELECT password, email, key FROM users WHERE username == "{username}";''')
        user_data = cursor.fetchone()
        cursor.close()

        if user_data is not None:
            data_handler = DataHandler(user_data[2])
            operation1, decrypted_password = data_handler.decrypt(user_data[0])
            operation2, decrypted_email = data_handler.decrypt(user_data[1])

            if operation1 and operation2:
                self.__send_email(decrypted_email, decrypted_password)
        return operation1 and operation2 and user_data is not None
    

    def get_last_user(self) -> tuple[str, str]:
        cursor = self.__connection.cursor()
        cursor.execute(f'''SELECT username, plain_password FROM users WHERE remember == TRUE''')
        user_data = cursor.fetchone()
        cursor.close()
        return user_data
    

    def __send_email(self, email: str, data) -> None:
        if data is None:
            pass
        else:
            pass


    def get_all_passwords(self) -> tuple[bool, list[Password]]:
        if not self.authenticated:
            return False, []
        
        cursor = self.__connection.cursor()
        cursor.execute(f'SELECT * FROM passwords WHERE user_id == "{self.__user_name}";')
        passwords = cursor.fetchall()
        cursor.close()

        passwords_list = []
        for password in passwords:
            operation, decrypted_data = self.__data_handler.decrypt_many(list(password[2:]))
            if not operation:
                return False, []
            
            password_data = list(password[:2]) + decrypted_data
            passwords_list.append(Password(*password_data))
        return True, passwords_list


    def get_password(self, password_id: str) -> tuple[bool, Password]:
        if not self.authenticated:
            return False, None
        
        cursor = self.__connection.cursor()
        cursor.execute(f'''SELECT * FROM passwords WHERE user_id = "{self.__user_name}" AND password_id = "{password_id}";''')
        password = cursor.fetchone()
        cursor.close()
        
        operation, decrypted_data = self.__data_handler.decrypt_many(list(password[2:]))
        if not operation:
            return False, None
        
        password_data = list(password[:2]) + decrypted_data
        return True, Password(*password_data)


    def add_password(self, password: Password) -> bool:
        operation, encrypted_data = self.__data_handler.encrypt_many(password.get_all()[2:])
        if not (self.authenticated and operation):
            return False
        
        password_id = str(uuid.uuid4())
        new_password = [password_id, self.__user_name] + encrypted_data

        cursor = self.__connection.cursor()
        query = f'''INSERT INTO passwords VALUES ({" ,".join(["?"] * len(new_password))})'''
        cursor.execute(query, new_password)
        cursor.close()
        self.__connection.commit()
        return True


    def update_password(self, password: Password) -> bool:
        operation, encrypted_data = self.__data_handler.encrypt_many(password.get_all()[2:])
        if not (self.authenticated and operation):
            return False
        
        new_password = encrypted_data + [password.owner, password.password_id]
        cursor = self.__connection.cursor()
        query = 'UPDATE passwords SET app_name = ?, app_username = ?, app_password = ?, app_email = ?, app_id = ?, app_url = ? WHERE user_id = ? AND password_id = ?;'
        cursor.execute(query, new_password)
        self.__connection.commit()
        cursor.close()
        return True
        
        
    def delete_password(self, id: list[str]) -> bool:
        if not self.authenticated:
            return False
        
        cursor = self.__connection.cursor()
        cursor.execute(f'DELETE FROM passwords WHERE password_id = "{id}";')
        cursor.close()
        self.__connection.commit()
        return True
