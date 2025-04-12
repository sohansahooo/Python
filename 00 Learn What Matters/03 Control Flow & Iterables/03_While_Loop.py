# While loop - Basic example
x = 0
while x < 4:
    print(x)
    x += 1  # Increment x



# Infinite loop example (commented to avoid infinite execution)
# while True:
#     print("This is an infinite loop") 

# While loop with break
x = 0
while x < 10:
    print(x)
    if x == 5:  # Exit loop when x reaches 5
        break
    x += 1



# While loop with continue
x = 0
while x < 6:
    x += 1
    if x % 2 == 0:
        continue  # Skip even numbers
    print(x)  # Only prints odd numbers



# While loop with else
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop ended without break")


