# There are built-in higher order functions
list(map(lambda x: x + 10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))  # => [6, 7]
