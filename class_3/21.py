def print_name():
    my_file = open("name.txt" , "r")
    for line in my_file.readlines():
        print(line, end="")

print_name()