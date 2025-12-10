#Name - Ekta Buneti
#Roll No- F077
#Q2 B: Write a program for Multiple inheritance (two base classes and 1 child class )
class Login:
    def login_details(self):
        return "Login successful."

class Profile:
    def profile_details(self):
        return "Profile loaded."

class UserAccount(Login, Profile):
    def __init__(self, username):
        self.username = username

    def show_account(self):
        print("Username:", self.username)
        print(self.login_details())
        print(self.profile_details())

u1 = UserAccount("ekta_123")
u1.show_account()
