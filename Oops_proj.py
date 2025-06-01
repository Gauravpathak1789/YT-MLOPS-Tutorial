class Chatboat:

    def __init__(self):
        self.username=""
        self.passwrd=""
        self.loggedin=False
        self.credentials_history={}
        self.menu()

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
            pass
        elif user_input=="4":
            pass
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



obj=Chatboat()