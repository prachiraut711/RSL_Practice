#49.convert binary to decimal using recursion

# A binary number is base-2.
# Each digit represents a power of 2.

# Example:

# binary:  1011
# places:   3 2 1 0
# decimal:  1*2^3 + 0*2^2 + 1*2^1 + 1*2^0
#         = 8 + 0 + 2 + 1 = 11

#WITHOUT USING RECURSION
def binary_to_decimal(str):
    decimal = 0
    power = 0
    for i in str[::-1]:  #as we de multiplivcation from left to right instead right to left
        if i not in ("0", "1"):
            return "Invalid binary number"
        
        decimal += int(i) * (2 ** power)
        power += 1
    return decimal

print(binary_to_decimal("1010"))


#WITH USING RECURSION
print("_______________________")
# 🔑 Logic for Recursion
# Suppose the binary number is "1010":
# "1010" =
# → left part "101" and last digit "0"
# So formula:
# Decimal(binary)=2×Decimal(prefix)+last_digit
# Where:
# prefix = all digits except last
# last_digit = last digit of the string

#jar last sodun adiche digit ch decimal madhe conversion kel ani tyala 2 ne maultiply ani last_digit ni add kel tar answer yet

def binary_to_decimal_recursive(str):
    if len(str) == 1:
        return int(str)
    
    last_dighit = int(str[-1])
    prefix = str[:-1]

    return 2 * binary_to_decimal_recursive(prefix) + last_dighit

# Example usage
print(binary_to_decimal_recursive("1010"))  # 10
print(binary_to_decimal_recursive("111"))   # 7
print(binary_to_decimal_recursive("1001"))  # 9
    


