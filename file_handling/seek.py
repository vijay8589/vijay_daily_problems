with open(r"D:\daily_problems\read_demo.txt", "r") as fp:
    # Moving the file handle to 6th character 
    fp.seek(3)
    # read file
    print(fp.read())



with open(r"D:\daily_problems\sample3.txt", "w+") as fp:
    # add content
    fp.write('My First Line\n')
    fp.write('My Second Line')
    # move pointer to the beginning
    fp.seek(0)
    # read file
    print(fp.read())