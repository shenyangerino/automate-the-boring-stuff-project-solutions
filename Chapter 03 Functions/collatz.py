# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer and that keeps calling collatz() on that number
# until the function returns the value 1.

# Add try and except statements to the previous project to detect whether the user types in a noninteger string.

def collatz(number):
    if number % 2 == 0:    # If number is even, collatz() will execute this
        result = number // 2
        return result
    else:    # If number is odd, collatz() will execute this
        result = 3 * number + 1
        return result

while True:    # The request for input loops until the user provides a positive integer
    number = input("Enter a positive integer: ")
    try:
        number_int = int(number)    # Validates that input is an integer
        if number_int < 1:    # Validates that input is a positive integer
            raise ValueError
        break
    except ValueError:
        print("The input must be a positive integer.")
        is_int = False

while number_int != 1:
    number_int = collatz(number_int)
    print(number_int)    #prints every iteration of the collatz() loop
