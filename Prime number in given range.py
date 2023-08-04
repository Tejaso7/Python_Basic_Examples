# to print prime number in given range

start = int(input("Enter start number : "))
end = int(input("Enter end number : "))
for a in range (start-1,end):
    a+=1
    for i in range(2, a):
        if (a % i) == 0:
            break
    else:
        print(a)
