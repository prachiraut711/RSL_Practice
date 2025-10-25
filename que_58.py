# nearest prime number of given number
# question:
# Given a number n, find the nearest prime number to it.
# If two primes are equally near (like for 8 → 7 and 11), return the smaller one.

# Algorithm:
# Check if n is prime
# If yes → return n.
# Otherwise, move outward from n:
# Check n - 1, n + 1, n - 2, n + 2, ... until you find the nearest prime.
# Return the first prime found.
# If both sides have a prime at equal distance, return the smaller one.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 - 1):
        if num % i == 0:
            return False
    return True

def nearest_prime_number(n):
    if is_prime(n):
        return n
    
    offset = 1
    while True:
        lower = n - 1
        higher = n + 1

        if lower >= 2 and is_prime(lower):
            return lower
        elif is_prime(higher):
            return higher
        
        offset += 1

print(nearest_prime_number(10))
print(nearest_prime_number(8))
print(nearest_prime_number(17))
print(nearest_prime_number(30))

# to return both nearest primes if they are equally distant from n.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nearest_prime(n):
    if is_prime(n):
        return [n]  # If n is already prime
    
    offset = 1
    while True:
        lower = n - offset
        higher = n + offset
        
        lower_prime = lower >= 2 and is_prime(lower)
        higher_prime = is_prime(higher)
        
        # If both primes found at same distance
        if lower_prime and higher_prime:
            return [lower, higher]
        elif lower_prime:
            return [lower]
        elif higher_prime:
            return [higher]
        
        offset += 1
print("____________")
print(nearest_prime(8))   # [7]
print(nearest_prime(9))   # [7, 11]
print(nearest_prime(10))  # [11]
print(nearest_prime(17))  # [17]
print(nearest_prime(30))
