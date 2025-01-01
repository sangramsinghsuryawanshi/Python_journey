# Create a tuple with different data types
my_tuple = (10, "apple", 3.14, True, "banana", 42, 10, "apple", False)

print(f"Original Tuple: {my_tuple}")

# a) Add an item in a tuple
# Tuples are immutable, so we create a new tuple by concatenation
new_item = "orange"
my_tuple = my_tuple + (new_item,)
print(f"Tuple after adding '{new_item}': {my_tuple}")

# b) Get the 4th element from the tuple
fourth_element = my_tuple[3]
print(f"The 4th element in the tuple is: {fourth_element}")

# c) Get the 4th element from the last of the tuple
fourth_last_element = my_tuple[-4]
print(f"The 4th element from the last in the tuple is: {fourth_last_element}")

# d) Find the occurrences of any repeated items
item_to_count = "apple"
occurrences = my_tuple.count(item_to_count)
print(f"The item '{item_to_count}' occurs {occurrences} times in the tuple.")

# e) Check whether an element exists within a tuple
element_to_check = 42
exists = element_to_check in my_tuple
print(f"Does the element '{element_to_check}' exist in the tuple? {exists}")

# f) Remove an item from a tuple
# Create a new tuple without the item (tuples are immutable)
item_to_remove = 10
my_tuple = tuple(x for x in my_tuple if x != item_to_remove)
print(f"Tuple after removing '{item_to_remove}': {my_tuple}")

# g) Get the first 3 elements in the tuple
first_three = my_tuple[:3]
print(f"The first 3 elements in the tuple are: {first_three}")

# h) Get any item by using index
index_to_get = 2
item_at_index = my_tuple[index_to_get]
print(f"The item at index {index_to_get} is: {item_at_index}")

# i) Find the length of a tuple
length = len(my_tuple)
print(f"The length of the tuple is: {length}")

# j) Reverse a tuple
reversed_tuple = my_tuple[::-1]
print(f"The reversed tuple is: {reversed_tuple}")
