# A-3: Sum of Prime Numbers in Array
# Algorithm

# Define a helper function is_prime(n) to check if a number is prime:

# Return False for numbers ≤ 1.

# Check divisibility from 2 to sqrt(n).

# Loop through the array.

# If an element is prime, add it to sum.

# If no prime numbers are found, print sum as 0.

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(arr):
    sum = 0
    for i in arr:
        if isPrime(i):
            sum += i
    return sum

print(sum_of_primes([1, 14, 5, 7]))   # Output: sum=12
print(sum_of_primes([2, 10, 13, 9])) # Output: sum=15print(sum_of_primes())
