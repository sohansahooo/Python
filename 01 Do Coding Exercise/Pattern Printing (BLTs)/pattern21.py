n = int(input("Enter the number of rows: "))

# Loop for rows
for i in range(n):
    for j in range(n):
        # Print asterisks on the borders
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
