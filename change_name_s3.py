import os
import shutil

file_oldname = os.path.join("C:\\Users\\Guilherme Massafera\\Desktop\\exportteste", "massafera.txt")
file_newname_newfile = os.path.join("C:\\Users\\Guilherme Massafera\\Desktop\\exportteste", "guilherme.txt")

newFileName = shutil.move(file_oldname, file_newname_newfile)

print("The renamed file has the name:", newFileName)

