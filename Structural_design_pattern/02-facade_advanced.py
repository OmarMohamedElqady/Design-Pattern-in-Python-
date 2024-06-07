
"""
Facade is a type of Structural Design Patterns
"""

"""Facade pattern with an example of user management system"""

"""
    A user management system in a software application.
    In this system, we have several processes such as creating a new user,
    updating user data, and deleting the user. We will simplify interaction 
    with these processes using a unified interface.
"""


class UserDatabase:
    def add_user(self, user_id, user_data):
        print(f"adding user {user_id} to the database with data :{user_data}")

    def update_user(self, user_id, user_data):
        print(f"updating user {user_id} to the database with data :{user_data}")

    def delete_user(self, user_id):
        print(f"Deleteing user {user_id} to the database")

class EmailServices:
    def Send_Welcome_Email(self, user_id):
        print(f"sending welcome email to user {user_id}")
        
    def Send_Update_Email(self, user_id):
        print(f"send Update email to user {user_id}")
        
    def Send_Goodbye_Email(self, user_id):
        print(f"send Goodbye email to user {user_id}")
        
class Logger:                       #Responsible for recording operations.
    def log(self, message):
        print(f"log : {message}")   #to record a specific message.

class UserManager:
    def __init__(self) :
        self.datbase = UserDatabase()
        self.emailServices = EmailServices()
        self.logger = Logger()        

    def createUser(self, user_id, user_data):
        self.datbase.add_user(user_id, user_data)
        self.emailServices.Send_Welcome_Email(user_id)
        self.logger.log(f"user {user_id} created")
    
    def updateUser(self, user_id, user_data):
        self.datbase.update_user(user_id, user_data)
        self.emailServices.Send_Update_Email(user_id)
        self.logger.log(f"user {user_id} updated")
    
    def deleteUser(self, user_id):
        self.datbase.delete_user(user_id)
        self.emailServices.Send_Goodbye_Email(user_id)
        self.logger.log(f"user {user_id} deleted")

if __name__ =="__main__":
    UserManager = UserManager()
    print("----Create User----")
    UserManager.createUser("123", {"name":"omar", "email": "OElqady@gmail.com"})
    print("\n----Update User----")
    UserManager.updateUser("123", {"name":"omar", "email": "OmarElqady@gmail.com"})
    print("\n----delete User----")
    UserManager.deleteUser("123")

