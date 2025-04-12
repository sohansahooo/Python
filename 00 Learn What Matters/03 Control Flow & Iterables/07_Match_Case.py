def print_multiplication_table(number):
    match number:
        case 1:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 2:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 3:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 4:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 5:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 6:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 7:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 8:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 9:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case 10:
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")
        case _:
            print("Number out of range, please enter a number between 1 and 10")

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number between 1 and 10: "))
    print_multiplication_table(number)
