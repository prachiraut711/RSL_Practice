# find the no's is odd or even by using only bitwise operator

# concept
# Every integer is stored in binary form.
# In binary:
# Even numbers always have their last bit = 0
# Odd numbers always have their last bit = 1

# num & 1
# If result = 0 → even
# If result = 1 → odd
# Because 1 in binary = 0001,
# and ANDing with 1 isolates only the last bit.

def check_odd_even(num):
    if num & 1:
        print(num, "is Odd")
    else:
        print(num, "is Even")

# Test
check_odd_even(10)
check_odd_even(7)
check_odd_even(0)
check_odd_even(15)
