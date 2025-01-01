# Program to read a text file and display its contents

# Specify the file name
file_name = input("Enter the file name to read: ").strip()

# Handle quotes around the file path, if present
if file_name.startswith('"') and file_name.endswith('"'):
    file_name = file_name[1:-1]

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read and display the contents
        print("\nContents of the file:")
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
