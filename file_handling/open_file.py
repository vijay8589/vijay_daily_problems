x = open(r"D:\daily_problems\python.txt", "r")
print(x.read())
x.close()




try:
    fp = open("python1.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("Please check the path.")




try:
    # Creating a new file
    with open("sample3.txt", "x") as fp:
        fp.write("Hello World! I am a new file")

    # reading the contents of the new file
    fp = open("sample3.txt", "r")
    print(fp.read())
except FileExistsError:
    print("The file already exists")




with open("Sample3.txt", "r+") as fp:
    # reading the contents before writing
    print(fp.read())

    # Writing new content to this file
    fp.write("\nAdding this new content")