# 17.count the number of different bits present in two integer number using bitwise operators

def countDifferentBits(a, b):
    xor_value = a ^ b
    count = 0
    while xor_value > 0:
        count += xor_value & 1   ## check last bit
        xor_value >>= 1   #divide kartey mi mahnun right shift vaprl right shift diveide kart na 2 ni ithe 13 ch 6 mag 3 mag 2 mag 0.tasch left shift 2 ne multiply kart jas 10 ch 20 jar <<2 asel 10 ch 20 ani 20 ch 40 as. ithe aplayla kami karych mahnun right shift divide val vaprl.
    return count

print(countDifferentBits(22, 27))
print(countDifferentBits(10, 20))
print(countDifferentBits(7, 7))


# Step-by-Step Example
# 22 = 10110
# 27 = 11011
# XOR = 01101(13) → has 3 ones → answer = 3
# Let’s take xor_val = 1101 (binary) which is 13 (decimal).

# Start:

# count = 0

# xor_val = 1101 (13)

# Iteration 1:

# xor_val & 1 = 1101 & 0001 = 1
# 👉 last bit is 1, so increment count.

# count = 1

# Right shift: xor_val = 1101 >> 1 = 110 (6)

# Iteration 2:

# xor_val & 1 = 0110 & 0001 = 0
# 👉 last bit is 0, don’t increment.

# count = 1

# Right shift: xor_val = 110 >> 1 = 11 (3)

# Iteration 3:

# xor_val & 1 = 0011 & 0001 = 1
# 👉 last bit is 1, so increment.

# count = 2

# Right shift: xor_val = 11 >> 1 = 1 (1)

# Iteration 4:

# xor_val & 1 = 0001 & 0001 = 1
# 👉 last bit is 1, so increment.

# count = 3

# Right shift: xor_val = 1 >> 1 = 0

# End:

# Loop stops (since xor_val = 0)

# Final count = 3

# ✅ There are 3 different bits between 6 (0110) and 11 (1011).

