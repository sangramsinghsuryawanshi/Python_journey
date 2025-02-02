with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

with open("sample.txt", "r") as file:
    print("Reading entire file:")
    print(file.read())

with open("sample.txt", "r") as file:
    print("\nReading one line at a time:")
    print(file.readline(), end="")  # Reads first line
    print(file.readline(), end="")  # Reads second line

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("\nReading all lines into a list:")
    print(lines)
