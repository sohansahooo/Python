# Basic iterable and iterator usage
my_dict = {"one": 1, "two": 2, "three": 3}

# Get iterable of dictionary keys
my_keys = my_dict.keys()

# Iterating over dictionary keys
for key in my_keys:
    print("Key:", key)

# Using iterator directly
my_iterator = iter(my_keys)
print("First key using iterator:", next(my_iterator))
print("Second key using iterator:", next(my_iterator))

# Catching StopIteration
try:
    while True:
        print(next(my_iterator))
except StopIteration:
    print("Reached the end of the iterator")
