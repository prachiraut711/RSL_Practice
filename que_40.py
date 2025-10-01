# 8.Decimal to binary 

def binary_to_decimal(num):
    if num == 0:
        return 0
    
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    return binary

print(binary_to_decimal(10))
print(binary_to_decimal(7))
print(binary_to_decimal(0))