# Lists: Python’s Dynamic Arrays
my_list = [1, 2, 3]

# Modifying lists with methods
my_list.append(4)          # Adds 4 at the end
my_list.insert(1, 'a')     # Inserts 'a' at index 1
print("List after insert:", my_list)

my_list.extend([5, 6, 7])  # Adds multiple elements at the end
print("List after extend:", my_list)

# Removing elements
my_list.pop()              # Removes the last item (7)
my_list.remove('a')        # Removes the first occurrence of 'a'
print("List after pop and remove:", my_list)

# Sorting and reversing
my_list.sort()             # Sorts the list in ascending order
my_list.reverse()          # Reverses the list
print("List after sort and reverse:", my_list)

# Other list operations
print("Length of list:", len(my_list))
print("Index of 3:", my_list.index(3))
print("Count of 3:", my_list.count(3))
