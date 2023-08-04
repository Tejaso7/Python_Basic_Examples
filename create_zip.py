from zipfile import ZipFile

with ZipFile("myZip.zip", "w") as z:
    z.write("mukund.txt")
    print("Zip file created ")