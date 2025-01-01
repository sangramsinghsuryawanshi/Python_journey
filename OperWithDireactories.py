# Create an initial dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Original Dictionary:", my_dict)

# a) Add a key to the dictionary
new_key = "profession"
new_value = "Engineer"
my_dict[new_key] = new_value
print(f"\nDictionary after adding '{new_key}': {my_dict}")

# b) Concatenate dictionaries to create a new dictionary
additional_dict = {"hobby": "painting", "country": "USA"}
concatenated_dict = {**my_dict, **additional_dict}  # Using dictionary unpacking
print("\nConcatenated Dictionary:", concatenated_dict)

# c) Check if a given key already exists in the dictionary
key_to_check = "age"
exists = key_to_check in my_dict
print(f"\nDoes the key '{key_to_check}' exist in the dictionary? {exists}")

# d) Remove a key from the dictionary
key_to_remove = "city"
if key_to_remove in my_dict:
    removed_value = my_dict.pop(key_to_remove)
    print(f"\nDictionary after removing '{key_to_remove}': {my_dict}")
else:
    print(f"\nKey '{key_to_remove}' not found in the dictionary.")

# e) Print a dictionary line by line
print("\nDictionary content line by line:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
