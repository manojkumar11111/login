class login():
    def __init__(self,username,password):
        if username.isalnum():
            self.username=username
        else:
            self.username=None
            print("username should contain alphabets and numbers only")
        if len(password)>=4:
            self.password=password
        else:
            self.password=None
            print("password should contain above 4 charcters")
    def is_valid_login(self):
        return self.username=="manoj" and self.password=="manoj@123"

usn=input("enter username ")
pwd=input("enter password ")
lg=login(usn,pwd)
if lg.is_valid_login():
    print("successfully login complete")
else:
    print("try again")
print(vars(lg))