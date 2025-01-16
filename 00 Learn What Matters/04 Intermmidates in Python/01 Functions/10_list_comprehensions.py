# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list (which itself may be nested).
print([i + 10 for i in [1, 2, 3]])  # => [11, 12, 13]
print([x for x in [3, 4, 5, 6, 7] if x >= 5])  # => [5, 6, 7]
