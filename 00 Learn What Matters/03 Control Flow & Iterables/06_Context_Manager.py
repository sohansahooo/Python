# Using with statement for file operations
data = {"name": "Alice", "age": 30}

# Write data to file
with open("data_file.txt", "w") as f:
    f.write(str(data))

# Read data from file
with open("data_file.txt", "r") as f:
    content = f.read()
    print("Read content:", content)
