text = "This is new content"
# writing new content to the file
fp = open("write_demo.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()

# Open the file for reading the new contents
fp = open("write_demo.txt", 'r')
print(fp.read())
fp.close()



file_path = r"D:\daily_problems\write_demo.txt"
fp = open(file_path, 'r')
print(fp.read())
fp.close()

# overwriting existing content of a file
fp = open(file_path, 'w')
fp.write("This is overwritten content")
fp.close()

# Read file
fp = open(file_path, 'r')
print("Opening file again..")
print(fp.read())
fp.close()





person_data = ['Name: Emma', '\nAddress: 221 Baker Street', '\nCity: London']
# writing string and list of lines to a file
fp = open("write_demo.txt", "w")
fp.writelines(person_data)
fp.close()

# opening the file in read mode
fp = open("write_demo.txt", "r")
print(fp.read())
fp.close()



name = '\nEmma'
address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
# append to file
with open("Write_demo.txt", "a") as f:
    f.write(name)
    f.writelines(address)

# opening the file in read mode to access the file
with open("Write_demo.txt", "r") as f:
    print(f.read())




name = '\nAntony'
address = ['\nAddress: 221 Baker Street', '\nCity: London', '\nCountry:United Kingdom']
# append to file
with open("Write_demo.txt", "a+") as f:
    f.write(name)
    f.writelines(address)
    # move file handle to the start
    f.seek(0)
    print(f.read())