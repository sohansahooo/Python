# This script determines if a given integer n is "Weird" or "Not Weird"
# based on specific conditions.

# Get user input and strip any surrounding whitespace
n = int(input("Your Number: ").strip())

# Check if the number is odd
if n % 2 != 0:
    # If n is odd, print "Weird"
    print("Weird")
else:
    # If n is even, further check the range of n
    if 2 <= n <= 5:
        # If n is even and in the range 2 to 5 inclusive, print "Not Weird"
        print("Not Weird")
    elif 6 <= n <= 20:
        # If n is even and in the range 6 to 20 inclusive, print "Weird"
        print("Weird")
    else:
        # If n is even and greater than 20, print "Not Weird"
        print("Not Weird")
