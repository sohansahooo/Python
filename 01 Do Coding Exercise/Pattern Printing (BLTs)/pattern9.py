n = int(input("Enter the number of rows: "))

# Loop for row
for i in range(n): 
    for j in range(n - i - 1): 
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()

for i in range(n): 
    for j in range(i): 
        print(" ", end="")
    for k in range(n - i):
        print("* ", end="")
    print()