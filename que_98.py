# 1. Count Numeric and Other Characters (A-1) Write a function int frequencyOfNumericChars(String input) that takes a string and prints: The count of each numeric character ('0' through '9'). 
# The count of all remaining characters (non-numerics). 
#ex. input= Raja1123labs output = "1"=2, "2"=1, "3"=1, others=8

# Count frequency of each digit (0–9) and total non-numeric characters.
# Logic:
# Initialize a list of size 10 for digits.
# Loop through each character:
# If it's a digit → increment its count.
# Else → increment “other” count.


def frequencyOfNumericChars(str):
    digits_count = [0] * 10
    others = 0
    for ch in str:
        if '0' <= ch <= '9':
            digits_count[int(ch)] += 1
        else:
            others += 1
    
    result = []
    for i in range(10):
        if digits_count[i] > 0:
            result.append(f'"{i}"= {digits_count[i]}')
    result.append(f'others= {others}')

    return ", ".join(result)

print(frequencyOfNumericChars("Raja1123labs"))