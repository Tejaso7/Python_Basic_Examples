f = open("mukund.txt")
print(f.read())
f.close()

f = open("mukund.txt",'r')
print(f.read())

print(f.tell())
f.seek(8)
print(f.seek(8))
print(f.read())


with open("mukund.txt", encoding = 'utf-8') as f:
    print(f.read())

#for line in f:
 #   print(line, end='')
#f.readline()

#Delete File
import os

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted !")
else:
    print("File does not exist !")


#f = open("sample.txt", "r+")
#f.seek(0)
#f.truncate()

#Rename File

#os.rename(src, dst)

#Rename  Multiple Files

#import os
#for count, filename in enumerate(os.listdir("xyz")):
#	dst ="Hostel" + str(count) + ".jpg"
#	src ='xyz'+ filename
#	dst ='xyz'+ dst
#	os.rename(src, dst)
