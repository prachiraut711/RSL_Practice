# 56. Write a function that prints out a breakdown of an integer intInput: 43018,
#     Output: Print 40000 + 3000 + 10 + 8
# Input: 43018
# 4 in the ten-thousands place → 40000
# 3 in the thousands place → 3000
# 0 in the hundreds place → skip
# 1 in the tens place → 10
# 8 in the ones place → 8

# 📌 Algorithm
# Convert integer into string to process each digit with its position.
# For each digit:
# Multiply it with 10^(position) to get its place value.
# If digit ≠ 0, keep it.
# Collect all non-zero values in a list.
# Join them with " + " and print.

def breakdownNum(num):
    num_str = str(num) #to iterate converted int to str
    n = len(num_str)
    parts = []
    for i, digit in enumerate(num_str):
        if digit != 0: #if 0 then skip
            place_value = int(digit) * (10 ** (n - i - 1))
            parts.append(str(place_value))   #parat int ch str kel ani append kel list madhe
    
    return " + ".join(parts)

print(breakdownNum(43018))


#  Dry Run for 43018
# num_str = "43018", n = 5
# i=0 → digit=4 → 4 * 10^(5-0-1) = 4*10000 = 40000
# i=1 → digit=3 → 3 * 1000 = 3000
# i=2 → digit=0 → skip
# i=3 → digit=1 → 1 * 10 = 10
# i=4 → digit=8 → 8 * 1 = 8
# Collected → ["40000", "3000", "10", "8"]
# Joined → "40000 + 3000 + 10 + 8" ✅

