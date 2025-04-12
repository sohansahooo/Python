# You can define functions that take a variable number of positional arguments
def varargs(*args):
    return args

print(varargs(1, 2, 3))  # => (1, 2, 3)

# You can define functions that take a variable number of keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

print(keyword_args(big="foot", loch="ness"))  # => {"big": "foot", "loch": "ness"}
