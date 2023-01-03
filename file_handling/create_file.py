file = open("python.txt", "w+")
file.close()

file1 = open("python1.txt", "w")
file1.write("first line")
file1.close()




import os

# list files from a working directory
print(os.listdir())

# verify file exist
print(os.path.isfile('python.txt'))