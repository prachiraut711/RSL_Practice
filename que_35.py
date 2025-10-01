# 42.check whether given number is strong number or not

# 🔹 Question: What is a Strong Number?
# A Strong Number (also called Krishnamurthy Number) is a number whose sum of the factorials of its digits is equal to the number itself.
# 👉 In simple words:
# Take each digit, find its factorial, add them all, and check if it equals the number.
# 🔹 Example
# 145
# Digits → 1, 4, 5
# 1!+4!+5!=1+24+120=145 ✅
# So, 145 is a Strong Number.

# 123
# Digits → 1, 2, 3
# 1!+2!+3!= 1+2+6= 9 = 123 ❌
# So, 123 is not a Strong Number.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def strongNumber(num):
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum += factorial(digit)
        num = num // 10
    

    if sum == temp:
        return "strong Number"
    else:
        return "Not strong number"

print(strongNumber(145))  #1! + 4! +5! =145 strong num
print(strongNumber(123))  #1! +2! + 3! = 9 not 123 so not strong num

        


