# Dictionaries: Key-Value Stores
my_dict = {"name": "Alice", "age": 25}

# Accessing values and adding/removing keys
print("Name in dictionary:", my_dict["name"])  # => Alice
my_dict["location"] = "Wonderland"
del my_dict["age"]
print("Dictionary after modifications:", my_dict)

# Using common dictionary methods
print("Keys:", my_dict.keys())           # Shows all keys
print("Values:", my_dict.values())       # Shows all values
print("Items:", my_dict.items())         # Shows all key-value pairs
print("Get 'location':", my_dict.get("location", "Unknown"))  # Safely get value
my_dict.update({"hobby": "reading"})     # Add a new key-value pair
print("Dictionary after update:", my_dict)
