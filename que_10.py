# Convert numerical string to int without using any Standard function

def convert(s):
    num = 0
    for i in s:
        digit = ord(i) - ord("0")
        num = num * 10 + digit
    return num
print(convert("123"))