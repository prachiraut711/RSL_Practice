# 15.prime number

# to check single number is prime or not
def prime_or_not(num):
    if num <= 1:
        return "Not Prime Not Composite"
    isPrime = True
    for i in range(2, num // 2 + 1):      # for n = 2 range(2, 2) is empty → loop never runs → isPrime stays True → returns True. for 3 also range will be (2,2) so not gonna in loop
        if num % i == 0:
            isPrime = False
            break
    
    if isPrime:
        return "Prime Number"
    else:
        return "Not Prime Number"

print(prime_or_not(int(input("enter no: "))))





#TO list out prime number in given RANGE for ex:here between in 1, 50 

def prime_or_not(n):
    if n <= 1:
        return False
    isPrime = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime

def prime_in_range(n):
    prime_numbers = []
    for i in range(2, n + 1):
        if prime_or_not(i):    #condition if prime_or_not(i) is True  hi condition ahe so jar isPrime false asel tar ya condition mdhe yenarch nahi ani mag append pn nahi honar
            prime_numbers.append(i)
    return prime_numbers



print(prime_in_range(50))

    
    
    
