# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}

all_the_args(*args)  # equivalent: all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)  # equivalent: all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent: all_the_args(1, 2, 3, 4, a=3, b=4)
