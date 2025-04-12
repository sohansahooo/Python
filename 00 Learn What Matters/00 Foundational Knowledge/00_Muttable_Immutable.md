# Mutable and Immutable Objects in Python

In Python, the terms **mutable** and **immutable** refer to the ability of an object to be changed after it is created.

## Mutable Objects
Mutable objects can be changed after they are created. This means you can modify their content without changing their identity. Common mutable types in Python include:

### 1. Lists
```python
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
print(my_list)  # Output: [10, 2, 3]
```

### 2. Dictionaries
```python
my_dict = {'a': 1, 'b': 2}
my_dict['a'] = 10  # Changing the value associated with key 'a'
print(my_dict)  # Output: {'a': 10, 'b': 2}
```

### 3. Sets
```python
my_set = {1, 2, 3, 4, 5}
print(my_set)   # Output: {1, 2, 3, 4, 5}
```


## Immutable Objects

Immutable objects cannot be changed after they are created. If you want to change an immutable object, you have to create a new object. Common immutable types in Python include:

### 1. Strings
```python
my_string = "hello"
new_string = my_string.replace('h', 'j')  # Creating a new string
print(new_string)  # Output: "jello"
print(my_string)   # Output: "hello" (original string unchanged)
```

### 2. Tuples
```python
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)  # Creating a new tuple
print(new_tuple)  # Output: (1, 2, 3, 4)
print(my_tuple)   # Output: (1, 2, 3) (original tuple unchanged)
```

### 3. Integers and Floats
```python
my_int = 5
new_int = my_int + 1  # Creating a new integer
print(new_int)  # Output: 6
print(my_int)   # Output: 5 (original integer unchanged)
```

Understanding the difference between mutable and immutable objects is crucial for writing efficient and bug-free code. It helps in making decisions about which data types to use in different scenarios.