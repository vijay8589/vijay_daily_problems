try:
    fp = open(r"D:\daily_problems\sample3.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("Please check the path")


try:
    # Creating a new file
    with open("read_demo.txt", "x") as fp:
        fp.write("first line")
        fp.write("\nsecond line")
        fp.write("\nthird line")
        fp.write("\nfourth line")
        fp.write("\nfifth line")

    # reading the contents of the new file
    fp = open("read_demo.txt", "r")
    print(fp.read())
except FileExistsError:
    print("The file already exists")



with open('read_demo.txt', 'r') as fp:
    # read first line
    # assign it to string variable
    line = fp.readline()
    print(line)


with open('read_demo.txt', 'r') as file:
    # read first 3 lines
    for i in range(3):
        print(file.readline().strip())