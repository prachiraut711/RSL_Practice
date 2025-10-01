# 43.Fibonacci series using recursion

# Formula: F(n) = F(n−1) + F(n−2)
# with base cases: F(0)=0,F(1)=1

# A Fibonacci Series is a sequence of numbers where:
# 👉 Each number is the sum of the previous two numbers.
# 👉 It starts with 0 and 1.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# 🔹 Algorithm
# Input how many terms (n) you want.

# Start with first two numbers → a = 0, b = 1.

# Print a and b.

# Loop from 3 to n:

# Next term = a + b.

# Print it.

# Update a = b, b = next_term.


#WITHOUT USING RECURSSION
def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("enter positive number")
    elif n == 1:
        print(a)
    else:
        print("Fibonacci series:")
        print(a, b, end = " ")
        for _ in range(2, n):   # _ this use if we dont want variable like i but we only want looping till rane
            c = a + b
            print(c, end = " ")
            a, b = b, c

fibonacci(10)
            
#USING RECURSSION
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)
    
n = 15
for i in range(n):
    print(fibonacci(i), end =" ")


# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Constraints:

# 0 <= n <= 30
# def fib(self, n):
#         a, b = 0, 1
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             for _ in range(2, n + 1):
#                 c = a + b
#                 a, b = b, c
#         return c

