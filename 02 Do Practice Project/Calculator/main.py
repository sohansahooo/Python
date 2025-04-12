try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))

    print(
        "\nWhat kind of operation do you want to perform?\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)"
    )

    o = int(input("Enter your choice: "))

    match o:
        case 1:
            print(f"The sum of {a} and {b} is {a + b}")
        case 2:
            print(f"The difference between {a} and {b} is {a - b}")
        case 3:
            print(f"The product of {a} and {b} is {a * b}")
        case 4:
            print(f"The quotient of {a} and {b} is {a / b}")
        case _:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
