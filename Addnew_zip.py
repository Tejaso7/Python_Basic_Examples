from zipfile import ZipFile
with ZipFile("path.zip", "a") as z:
    z.write("mukund.txt")