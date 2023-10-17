# bot at class entrance
user = ["Tejas", "Ulkesh", "Suraj", "Samiksha", "Vaishnavi", "Avdhoot"]
block = ["Sameer"] 
#this is simple code

#Sameer has refused admission so not allow them where Swapnil want to join but he is in confusion
while True:
    name = input("enter your name : ")
    print("Hello", name)
    if name in user :
        print("You can join Training !")
    elif name in block :
        print(" You are not allowed in training session ")
    else :
        print("Wait ultill someone allow you")
        print("Bellow message is sent to Akshay Sir ")
        yes = str(input("Type Yes if you want to add this person into training : "))
        if yes == "Yes":
            user.append(name)
            print(name, "you are added into class and Now you can join the Training session")
        else:
            print("Sorry Your are not allowed")






'''
#  Admin = "Vaishnavi"
family_member = ("Vaishnavi", "Dhanashree","Radhika" "saniksha","Poonan")
while True :
    Name = input("please enter your name")
    if Name in family_member :
        print("welcome" + Name)
    else :
        print("Asking for permission")
        permission = int(input("type 1 if want to allow : "))
        if permission == 1:
            print(" your welcome")
        else:
            print("contact user ")

'''
