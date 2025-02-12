"""
For Loop:
"""
# Read the integer from input
n = int(input("Your Number: ").strip())

# Loop through all non-negative integers less than n
for i in range(n):
    # Print the square of each number
    print(i * i)



"""
While Loop:
"""
# Read the integer from input
n = int(input("Your Number: ").strip())

# Initialize the counter
i = 0

# Use a while loop to iterate through all non-negative integers less than n
while i < n:
    # Print the square of each number
    print(i * i)
    # Increment the counter
    i += 1
