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
        user_data = cursor.fetchall()
        cursor.close()

        passwords = []
        for row in user_data:
            operation, decrypted_data = self.__data_handler.decrypt_many(list(row[2:]))
            if not operation:
                return False, []
            
            password_data = list(row[:2]) + decrypted_data
            passwords.append(Password(*password_data))
        return True, passwords


    def get_password(self, password_id: str) -> tuple[bool, list[str]]:
        if not self.authenticated:
            return False, None
        
        cursor = self.__connection.cursor()
        cursor.execute(f'''SELECT password_id, app_name, app_username, app_password, app_email, app_id, app_url FROM passwords WHERE user_id = "{self.__user_name}" AND password_id = "{password_id}";''')
        data = cursor.fetchone()
        cursor.close()
        
        password_id = data[0]
        op1, app_name = self.__data_handler.decrypt(data[1])
        op2, app_username = self.__data_handler.decrypt(data[2])
        op3, app_password = self.__data_handler.decrypt(data[3])
        op4, app_email = self.__data_handler.decrypt(data[4])
        op5, app_id = self.__data_handler.decrypt(data[5])
        op6, app_url = self.__data_handler.decrypt(data[6])

        operation = op1 and op2 and op3 and op4 and op5 and op6
        if not operation:
            return False, None
        
        return True, [password_id, app_name, app_username, app_password, app_email, app_id, app_url]


    def add_password(self, data: list[str]) -> bool:
        password_id = str(uuid.uuid4())
        op1, app_name = self.__data_handler.encrypt(data[1])
        op2, app_username = self.__data_handler.encrypt(data[2])
        op3, app_password = self.__data_handler.encrypt(data[3])
        op4, app_email = self.__data_handler.encrypt(data[4])
        op5, app_id = self.__data_handler.encrypt(data[5])
        op6, app_url = self.__data_handler.encrypt(data[6])
        operation = op1 and op2 and op3 and op4 and op5 and op6

        if not (self.authenticated and operation):
            return False
        
        new_password = [password_id, self.__user_name, app_name, app_username, app_password, app_email, app_id, app_url]
        cursor = self.__connection.cursor()
        query = f'''INSERT INTO passwords VALUES ({" ,".join(["?"] * len(new_password))})'''
        cursor.execute(query, new_password)
        self.__connection.commit()
        cursor.close()
        return True


    def update_password(self, data: list[str]):
        password_id = data[0]
        op1, app_name = self.__data_handler.encrypt(data[1])
        op2, app_username = self.__data_handler.encrypt(data[2])
        op3, app_password = self.__data_handler.encrypt(data[3])
        op4, app_email = self.__data_handler.encrypt(data[4])
        op5, app_id = self.__data_handler.encrypt(data[5])
        op6, app_url = self.__data_handler.encrypt(data[6])
        operation = op1 and op2 and op3 and op4 and op5 and op6

        if not (self.authenticated and operation):
            return False
        
        new_password = (app_name, app_username, app_password, app_email, app_id, app_url, self.__user_name, password_id)
        cursor = self.__connection.cursor()
        query = f'''UPDATE passwords SET app_name = ?, app_username = ?, app_password = ?, app_email = ?, app_id = ?, app_url = ? WHERE user_id = ? AND password_id = ?'''
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
