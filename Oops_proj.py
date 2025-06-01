class Chatboat:
    
    
    __user_id=0

    def __init__(self):
        self.__id=Chatboat.__user_id
        Chatboat.__user_id += 1
        self.__name="default user"
        self.username=""
        self.passwrd=""
        self.loggedin=False
        self.credentials_history={}
        # self.menu()

    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name=new_name

    @staticmethod
    def get_id():
        return Chatboat.__user_id

    @staticmethod
    def set_id(id):
        Chatboat.__user_id=id

    def menu(self):
        user_input=input("""Welcome to chatboat !! How would you like to proceed ?-
                            1.Press 1 to signup
                            2.Press 2 to sigin
                            3.Press 3 to write a post
                            4.Press 4 to message a friend
                            5.Press any other key to exit\n""")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.message_friend()
        else:
            exit()
    

    def signup(self):
        self.username=input("Enter your email :-->  ")
        self.passwrd=input("Enter your password :-->  ")
        self.credentials_history[self.username]=self.passwrd
        print("You have successfully signed up!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username=="" or self.passwrd=="":
            print("Please signup first!")
            self.menu()
        else:
            user_input=input("Enter your email :-->  ")
            pass_input=input("Enter your password :-->  ")
            if self.credentials_history.get(user_input) == pass_input:
                print("You have successfully signed in!")
                self.loggedin=True
            else:
                print("Invalid credentials, please try again.")
        print("\n")
        self.menu()

    def my_post(self):
        if not self.loggedin:
            print("Please sign in to write a post.")
            self.menu()
        else:
            post_content = input("Write your post: ")
            print(f"Post '{post_content}' has been written successfully!")
        print("\n")
        self.menu()
    

    def message_friend(self):
        if not self.loggedin:
            print("Please sign in to message a friend.")
            self.menu()
        else:
            friend_email = input("Enter your friend's email: ")
            message_content = input("Write your message: ")
            print(f"Message to {friend_email} has been sent successfully!")
        print("\n")
        self.menu()


obj=Chatboat()
obj2=Chatboat()
# t=obj.get_name()
# print(t)
# print(obj.id)
# print(obj2.id)
print(obj.get_id())
obj.set_id(9)
print(obj2.get_id())