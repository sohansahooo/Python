# Arithmetic Operators
x = 10
y = 3

print("Arithmetic Operators:")
print(f"x + y = {x + y}")      # Addition
print(f"x - y = {x - y}")      # Subtraction
print(f"x * y = {x * y}")      # Multiplication
print(f"x / y = {x / y}")      # Division
print(f"x // y = {x // y}")    # Floor Division
print(f"x % y = {x % y}")      # Modulo
print(f"x ** y = {x ** y}")    # Exponentiation

# Comparison Operators
print("\nComparison Operators:")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Logical Operators
a = True
b = False
print("\nLogical Operators:")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

# Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("\nIdentity Operators:")
print(f"list1 is list2: {list1 is list2}")       # True, same object
print(f"list1 is list3: {list1 is list3}")       # False, different objects

# Membership Operators
print("\nMembership Operators:")
print(f"2 in list1: {2 in list1}")
print(f"4 not in list1: {4 not in list1}")

# Bitwise Operators
print("\nBitwise Operators:")
print(f"x & y: {x & y}")    # AND
print(f"x | y: {x | y}")    # OR
print(f"x ^ y: {x ^ y}")    # XOR
print(f"~x: {~x}")          # NOT
print(f"x << 1: {x << 1}")  # Left Shift
print(f"x >> 1: {x >> 1}")  # Right Shift
