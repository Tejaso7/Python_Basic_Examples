# printing prime number using while loop
a=5
i=0
while a<50:
    a +=1
    while 2 <= i < a:
        if (a % i) == 0:
            break
        i+=1
    else :
        print(a)
