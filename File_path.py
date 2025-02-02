file_path = "sangram.txt"

with open(file_path, "w") as file:
    file.write("Hello, this is a sangram file.\n") 
    lines = ["This is the second line.\n", "This is the third line.\n", "This is the fourth line.\n"]
    file.writelines(lines) 
with open(file_path, "r") as file:
    content = file.read()
    print("\nReading entire file using read():")
    print(content)

with open(file_path, "r") as file:
    print("\nReading first line using readline():")
    print(file.readline())

with open(file_path, "r") as file:
    print("\nReading all lines using readlines():")
    print(file.readlines())
