# Define two sets S and D
S = {'a', 'b', 'c', 'd'}
D = {'c', 'd', 'e', 'f'}
print(f"Set S: {S}")
print(f"Set D: {D}")

# a) Add 'g' to the set S
S.add('g')
print(f"\nSet S after adding 'g': {S}")

# b) Display the difference of the two sets (S - D)
difference = S.difference(D)
print(f"\nDifference of S and D (S - D): {difference}")

# c) Display the common values in set S and D (intersection)
common_values = S.intersection(D)
print(f"\nCommon values in S and D: {common_values}")

# d) Check whether set S is a subset of D
is_subset = S.issubset(D)
print(f"\nIs S a subset of D? {is_subset}")

# e) Check whether D is a superset of S
is_superset = D.issuperset(S)
print(f"\nIs D a superset of S? {is_superset}")

# f) Remove 'a' from set S
S.discard('a')  # Use discard to avoid KeyError if 'a' is not present
print(f"\nSet S after removing 'a': {S}")

# g) Display the values that are in S and in D but not in both (symmetric difference)
symmetric_difference = S.symmetric_difference(D)
print(f"\nValues in S and D but not in both: {symmetric_difference}")

# h) Take the union of two sets
union_sets = S.union(D)
print(f"\nUnion of S and D: {union_sets}")

# i) Remove all elements from set S
S.clear()
print(f"\nSet S after removing all elements: {S}")
