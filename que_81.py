# you need to check whether a given number is a Fibonacci number or not, and depending on that, 
# print either the number itself or the sum of even Fibonacci numbers less than it.

# Algorithm
# Generate Fibonacci numbers up to the given number.
# Check if the number exists in the Fibonacci sequence.
# If yes → print the number.
# If not → add up even Fibonacci numbers less than that number.

# Helper Logic: Check if a number is Fibonacci
# A number n is Fibonacci if and only if one of these is a **perfect square**:
# 5*n² + 4
# 5*n² - 4

def is_perfect_square(x):
    s = int(x ** 0.5)
    return s * s == x

def is_fibonacci(num):
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

def sum_even_fibonacci_less_than(n):
    a, b = 0, 1
    total = 0
    while b < n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

n = int(input("Enter a number: "))
if is_fibonacci(n):
    print(n)
else:
    print(sum_even_fibonacci_less_than(n))

