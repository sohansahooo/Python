# 1. Basic for loop with a list
animals = ["dog", "cat", "mouse"]
for animal in animals:
    print(f"{animal} is a mammal")



# 2. For loop with range (0 to 3)
for i in range(4):
    print(i)



# 3. For loop with range and custom start/stop (4 to 7)
for i in range(4, 8):
    print(i)



# 4. Using range with step (4 to 7 with step 2)
for i in range(4, 8, 2):
    print(i)



# 5. Loop with enumerate to get index and value
for index, animal in enumerate(animals):
    print(f"Index {index}: {animal}")



# 6. Looping over dictionaries
my_dict = {"name": "Alice", "age": 25, "city": "Wonderland"}

# Looping over keys
for key in my_dict:
    print(f"Key: {key}")

# Looping over values
for value in my_dict.values():
    print(f"Value: {value}")

# Looping over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")



# 7. List Comprehension Example
squared_numbers = [x**2 for x in range(5)]
print(f"Squared numbers: {squared_numbers}")
# Output: [0, 1, 4, 9, 16]


# 8. Nested for loop (2D list)
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for element in row:
        print(element)



# 9. for loop with else (Search with break)
numbers = [1, 2, 3, 4, 5]
target = 6
for number in numbers:
    if number == target:
        print("Found the target!")
        break
else:
    print("Target not found.")



# 10. for loop with zip (Iterating over multiple lists in parallel)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

