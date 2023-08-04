
#to print revese the list using for loop

list = ["python","learning","am","I",23,"is","age","my","Mukund","am","I"]

print("List is :", list)


c = len(list)
for i in range (0, c):
    i+=1
    reverse=list[-i]
    print(reverse)
