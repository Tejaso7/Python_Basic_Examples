import zipfile
with zipfile.ZipFile("D:/Learn/Python/Daily projects/myZip.zip", 'r') as zip:
    zip.printdir()
    zip.extractall("D:/Learn/myZip")