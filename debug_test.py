#!/usr/bin/env python3
"""
Simple Python script to test nvim-dap debugging functionality.
"""

def calculate_factorial(n):
    """Calculate factorial of n using iteration."""
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    """Main function to test the debugging features."""
    print("=== Python Debugging Test ===")
    
    # Test factorial calculation
    numbers = [0, 1, 5, 10]
    print("\nFactorial calculations:")
    for num in numbers:
        factorial_result = calculate_factorial(num)
        print(f"factorial({num}) = {factorial_result}")
    
    # Test Fibonacci sequence
    print("\nFibonacci sequence:")
    for i in range(1, 11):
        fib_result = fibonacci(i)
        print(f"fibonacci({i}) = {fib_result}")
    
    # Interactive part
    try:
        user_input = int(input("\nEnter a number to calculate its factorial: "))
        user_factorial = calculate_factorial(user_input)
        if user_factorial is not None:
            print(f"factorial({user_input}) = {user_factorial}")
        else:
            print("Cannot calculate factorial of negative numbers!")
    except ValueError:
        print("Please enter a valid integer.")
    
    print("\n=== Test completed ===")

if __name__ == "__main__":
    main()

