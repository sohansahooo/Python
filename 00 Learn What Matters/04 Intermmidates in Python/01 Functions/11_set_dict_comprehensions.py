# You can construct set and dict comprehensions as well.
print({x for x in "abcddeef" if x not in "abc"})  # => {'d', 'e', 'f'}
print({x: x**2 for x in range(5)})  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
