n = int(input("Enter the number of rows: "))

# Loop for row
for i in range(1, n + 1):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()
