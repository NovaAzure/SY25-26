file_name =  input("Enter filename:")
pattern = input("Enter pattern:")

file = open(file_name, "r")
line = file.readline()

while line:
    if pattern in line:
        print(file_name, line_strip())
    line = file.readline()
