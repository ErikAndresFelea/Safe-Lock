import uuid
import sqlite3 as sql
from code.login import Login
from code.register import Register
from code.dataHandler import DataHandler

class Controller:
    def __init__(self, connection: sql.Connection):
        super().__init__()
        self.authenticated = False
        self._connection = connection
        self._user_name: str = None
        self._data_handler: DataHandler = None
        

    def login(self, username: str, password: str, remember: bool) -> bool:
        login = Login(self._connection, username, password, remember)
        
        if login.authenticated:
            self._user_name = login.user_name
            self._data_handler = login.data_handler
            self.authenticated = login.authenticated
        return login.authenticated
    
    
    def register(self, username: str, email: str, password: str) -> bool:
        register = Register(self._connection, username, password, email)
        
        if register.registered:
            self._send_email(email, None)
        return register.registered


    def forgot_password(self, username: str) -> bool:
        cursor = self._connection.cursor()
        cursor.execute(f'''SELECT password, email, key FROM users WHERE username == "{username}";''')
        user_data = cursor.fetchone()
        cursor.close()

        if user_data is not None:
            data_handler = DataHandler(user_data[2])
            operation1, decrypted_password = data_handler.decrypt(user_data[0])
            operation2, decrypted_email = data_handler.decrypt(user_data[1])

            if operation1 and operation2:
                self._send_email(decrypted_email, decrypted_password)
        return operation1 and operation2 and user_data is not None
    

    def get_last_user(self) -> tuple[str, str]:
        cursor = self._connection.cursor()
        cursor.execute(f'''SELECT username, plain_password FROM users WHERE remember == TRUE''')
        user_data = cursor.fetchone()
        cursor.close()
        return user_data
    

    def _send_email(self, email: str, data) -> None:
        if data is None:
            pass
        else:
            pass


    def get_all_passwords(self) -> tuple[bool, list[list[str]]]:
        if self.authenticated:
            cursor = self._connection.cursor()
            cursor.execute(f'''SELECT password_id, app_name, app_username, app_password, app_email, app_id, app_url FROM passwords WHERE user_id == "{self._user_name}";''')
            user_data = cursor.fetchall()
            cursor.close()

            passwords = []
            operation = False
            for row in user_data:
                password_id = row[0]
                op1, app_name = self._data_handler.decrypt(row[1])
                op2, app_username = self._data_handler.decrypt(row[2])
                op3, app_password = self._data_handler.decrypt(row[3])
                op4, app_email = self._data_handler.decrypt(row[4])
                op5, app_id = self._data_handler.decrypt(row[5])
                op6, app_url = self._data_handler.decrypt(row[6])

                operation = op1 and op2 and op3 and op4 and op5 and op6
                if not operation:
                    passwords = []
                    break

                passwords.append([password_id, app_name, app_username, app_password, app_email, app_id, app_url])
            return operation, passwords
        return self.authenticated, []


    def get_password(self, password_id: str):
        pass


    def add_password(self, data: list[str]) -> bool:
        if self.authenticated:
            password_id = str(uuid.uuid4())
            op1, app_name = self._data_handler.encrypt(data[1])
            op2, app_username = self._data_handler.encrypt(data[2])
            op3, app_password = self._data_handler.encrypt(data[3])
            op4, app_email = self._data_handler.encrypt(data[4])
            op5, app_id = self._data_handler.encrypt(data[5])
            op6, app_url = self._data_handler.encrypt(data[6])

            operation = op1 and op2 and op3 and op4 and op5 and op6
            if operation:
                new_password = [password_id, self._user_name, app_name, app_username, app_password, app_email, app_id, app_url]
                cursor = self._connection.cursor()
                query = f'''INSERT INTO passwords VALUES ({" ,".join(["?"] * len(new_password))})'''
                cursor.execute(query, new_password)
                self._connection.commit()
                cursor.close()
            return operation
        return self.authenticated


    def update_password(self, data: list[str]):
        pass


    def delete_password(self, id: list[str]):
        pass


#    ''' Not used yet
#    def get_password(self, id: str) -> tuple[bool, list[str] | None]:
#        confirm, password = self.password_manager.get_password(id)
#        return confirm, password
#    '''
#
#    def update_password(self, data: list[str]) -> tuple[Error, Operation, Msg]:
#        return self.password_manager.update_password(data)
#
#    def delete_password(self, id: list[str]) -> tuple[Error, Operation, Msg]:
#        return self.password_manager.delete_password(id)
    