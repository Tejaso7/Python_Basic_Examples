# to print pattern
'''
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1          '''



for i in range (1,6):
    for j in range (1,6):
        if j>i:
            break

        print("*", end=" ")
    print()
for i in range(0, 6):
    for j in range(5- i, 0, -1):
        print("*", end=' ')
    print()
