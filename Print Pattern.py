# to print pattern
'''     1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''
#k=6
for i in range(0, 6):
    for j in range(6-i,0,-1):
        print(" ",end=" ")
    #k = k - 1
    for j in range(1, i+1):
        print(j, end=" ")
    print("")


# or this program can also work
'''
k=6
for i in range(0, 6):
    for j in range(0,k):
        print(" ",end=" ")
    k = k - 1
    for j in range(1, i+1):
        print(j, end=" ")
    print("")
'''