class user:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email = input("Enter email : ")
        password = input("Enter password : ")

        if email == self.email and password == self.password:
            login= True
            print("Login Successful!")
        else:
            print("Login Faild!")

    def logout(self):
         login = False
         print("Logged Out!")
         
    def isLoggedIn(self):
          if self.login:
              return True
          else:
              return False
          
    def profle(self):
          if isLoggedIn():
           print(self.name , "\n", self.email)
          else:
              print("User is not Logged in !")

user1 = user()
    
user1.name = "Mustakur"
user1.email = "bmrahman24@gmail.com"
user1.password="123456"
user1.login()

hello = input()
          

