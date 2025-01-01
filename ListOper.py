# Create the list
machine = [100, 850, 600, 210, 99, 23, 56, 777, 428, 657, 21]
print(f"Original list: {machine}")

# a) Remove 428 from the list
machine.remove(428)
print(f"After removing 428: {machine}")

# b) Get the index of 600
index_600 = machine.index(600)
print(f"Index of 600: {index_600}")

# c) Insert 1414 in the list after 777
index_777 = machine.index(777)
machine.insert(index_777 + 1, 1414)
print(f"After inserting 1414 after 777: {machine}")

# d) Extend the list by adding [999, 888]
machine.extend([999, 888])
print(f"After extending the list with [999, 888]: {machine}")

# e) Count the occurrences of 210
count_210 = machine.count(210)
print(f"Occurrences of 210: {count_210}")

# f) Sort the list
machine.sort()
print(f"After sorting: {machine}")

# g) Reverse the list
machine.reverse()
print(f"After reversing: {machine}")

# h) Display the last four values
last_four = machine[-4:]
print(f"Last four values: {last_four}")

# i) Remove the last value of the list
removed_value = machine.pop()
print(f"Removed last value: {removed_value}")
print(f"Updated list after removing last value: {machine}")
