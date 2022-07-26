class User:

    def __init__(self,fname,lname,city):
        self.fname=fname
        self.lname=lname
        self.city=city

class Bio(User):

    def __init__(self,fname,lname,city,email,about):
        User.__init__(self,fname,lname,city)
        self.email=email
        self.about=about

    def printdetails(self):
        print(f"\n Thank you for your registration {self.fname}.")


if __name__ == '__main__':
        try:
            fname = input("Enter your first name :")
            lname = input("Enter your last name :")
            city = input("Enter your city name :")
            email = input("Enter your email name :")
            about = input("Tell me about your self :")

            users= Bio(fname,lname,city,email,about)

            with open("users.txt","w") as f:
                f.write(f"Users Details are as follow :\n First name :{fname} \n Last name :{lname} \n City :{city} \n "
                        f"Email of user :{email} \n User about section :{about}")

            users.printdetails()

        except Exception as e:
            print(e)