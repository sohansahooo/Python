# Sets: Unique Collections
my_set = {1, 2, 3, 4}

# Adding and removing elements
my_set.add(5)
my_set.discard(2)   # Removes 2; doesn't throw an error if 2 isn't found
print("Set after add and discard:", my_set)

# Set operations
another_set = {3, 4, 5, 6}
print("Intersection:", my_set & another_set)  # => {3, 4, 5}
print("Union:", my_set | another_set)         # => {1, 3, 4, 5, 6}
print("Difference:", my_set - another_set)    # => {1}
print("Symmetric Difference:", my_set ^ another_set)  # => {1, 6}

# Checking subsets and supersets
print("Is my_set a subset of another_set?", my_set <= another_set)
print("Is my_set a superset of another_set?", my_set >= another_set)

# Checking for elements
print("Does my_set contain 3?", 3 in my_set)
print("Does my_set contain 10?", 10 in my_set)

# Copying the set
my_set_copy = my_set.copy()
print("Copied set:", my_set_copy)
