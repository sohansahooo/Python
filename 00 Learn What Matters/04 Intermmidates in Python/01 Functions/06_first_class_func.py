# Python has first-class functions
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
print(add_10(5))  # => 15
