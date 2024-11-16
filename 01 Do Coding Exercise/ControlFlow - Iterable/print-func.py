"""
This program reads an integer from standard input and prints a sequence of 
consecutive integers starting from 1 up to that integer, all in one line without spaces.
"""

if __name__ == '__main__':
    # Read an integer from standard input
    n = int(input("Enter an integer: "))
    
    # Initialize an empty string to store the result
    result = ''
    
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Convert the current number to a string and concatenate it to the result
        result += str(i)
    
    # Print the final result
    print(result)
