# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main program
if __name__ == "__main__":
    # Greet the user
    name = input("Enter your name: ")
    greet_user(name)
    
    # Add two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
    
    # Calculate factorial
    num = int(input("Enter a number to find its factorial: "))
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")
