n = int(input("Enter the number of rows: "))

# Loop for each row
for i in range(1, n+1):
    # Loop to print i in each column
    for j in range(1, i+1):
        print(i, end=" ")
    # Print a new line after each row
    print()