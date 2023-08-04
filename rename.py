import os
for count, filename in enumerate(os.listdir("D:/Learn/Python/Daily projects")):
    dst ="Hostel" + str(count) + ".jpg"
    src ='xyz'+ filename
    dst ='xyz'+ dst
    os.rename(src, dst)
