mail_id =input("Enter your email id :")
mname=mail_id.rsplit("@")[0]
# print(mname)
fname =mname.split(".")[0]
lname=mname.split(".")[1]

print(f"First name of user email is :{fname} and last name is {lname}")