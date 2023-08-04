#email slicing

email = input("Enter email ID : ")

print(email.index("@"))
print(email.index("."))

username = email[0:email.index("@")]
print("Username : ", username)

company_name = email[1+email.index("@"):email.index(".")]
print("Company Name : " , company_name)

