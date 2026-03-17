# ------------------------------------------
# Program: Factorial using Recursion
# ------------------------------------------

# Function to calculate factorial
def factorial(n):
    """
    This function returns the factorial of a number using recursion.
    factorial(n) = n * factorial(n-1)
    """

    # Base Case
    if n == 0 or n == 1:
        return 1

    # Recursive Case
    else:
        return n * factorial(n - 1)


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():
    print("=== Factorial Calculator (Recursion) ===")

    try:
        # Taking input from user
        num = int(input("Enter a non-negative integer: "))

        # Checking for negative numbers
        if num < 0:
            print("Factorial is not defined for negative numbers!")

        else:
            result = factorial(num)

            print(f"\nFactorial of {num} is: {result}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


# ------------------------------------------
# Program Execution Starts Here
# ------------------------------------------

if __name__ == "__main__":
    main()
