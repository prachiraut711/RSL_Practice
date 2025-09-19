# 5.Division of 2 numbers without using / and % operator

class Solution(object):
    def divide(self, dividend, divisor):
        if(dividend == divisor):
            return 1

        sign = True 
        if(dividend >= 0 and divisor < 0):
            sign = False
        elif(dividend < 0 and divisor  > 0):
            sign = False

        n = abs(dividend)
        d = abs(divisor)
        quotient = 0
        while n >= d:
            cnt = 0
            while n >= (d << (cnt + 1)):
                cnt += 1
            quotient += (1 << cnt)
            n -= (d << cnt)

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        if(quotient == (1 << 31) and sign):
            return INT_MAX
        elif(quotient == (1 << 31) and not sign):
            return INT_MIN

        if sign:
            return quotient 
        else:
            return -quotient
        

result = Solution()
ans = result.divide(22, 7)
print(ans)
# Line-by-line explanation (conceptual)


# if (dividend == divisor) return 1;
# Quick special case: if both numbers are equal, quotient is 1.

# Determine the sign of the final result:

# bool sign = true;
# if ((dividend >= 0 && divisor < 0) || (dividend <= 0 && divisor > 0))
#     sign = false;


# If exactly one of dividend or divisor is negative, the result is negative.

# Convert to non-negative values and use a wider type (long) to avoid overflow:

# long n = abs(dividend);
# long d = abs(divisor);


# n = absolute dividend, d = absolute divisor.

# long quotient = 0; — start with zero quotient.

# Outer loop: while (n >= d) { ... } — as long as the remaining n is at least d, we can subtract something.

# Inner loop finds the largest shift cnt such that d << (cnt+1) is still ≤ n:

# int cnt = 0;
# while (n >= (d << (cnt + 1))) cnt++;


# That means d << cnt is the largest doubled multiple of d fitting in n.

# Update quotient and remainder:

# quotient += 1 << cnt;     // add 2^cnt to quotient
# n -= (d << cnt);          // subtract d * (2^cnt) from n


# So you’ve accounted for d * 2^cnt in the quotient.

# After the loop, handle overflow per problem statement: if quotient equals 2^31 (out of signed 32-bit range) return INT_MAX or INT_MIN depending on sign.

# Finally return sign ? quotient : -quotient;.

# Why bit shifting?

# d << k = d * 2^k. Instead of subtracting d one by one, you subtract big chunks (d, 2d, 4d, 8d, ...) so the loop runs in about logarithmic steps.

# Walkthrough with dividend = 22, divisor = 3

# I'll compute every arithmetic step:

# Start:

# dividend = 22

# divisor = 3

# dividend == divisor? No, 22 ≠ 3 → continue.

# sign? Both positive → sign = true.

# n = abs(22) = 22

# d = abs(3) = 3

# quotient = 0

# Outer loop iteration 1 (n = 22, d = 3):

# Set cnt = 0.

# Check n >= d << (cnt+1) i.e. 22 >= 3 << 1:

# 3 << 1 = 3 * 2 = 6.

# 22 >= 6 → true → increment cnt → cnt = 1.

# Check 22 >= 3 << (1+1) i.e. 22 >= 3 << 2:

# 3 << 2 = 3 * 4 = 12.

# 22 >= 12 → true → increment cnt → cnt = 2.

# Check 22 >= 3 << (2+1) i.e. 22 >= 3 << 3:

# 3 << 3 = 3 * 8 = 24.

# 22 >= 24 → false → stop inner loop. Final cnt = 2.

# Update:

# quotient += 1 << cnt → quotient += 1 << 2 → 1 << 2 = 4 → quotient = 0 + 4 = 4.

# n -= d << cnt → n -= 3 << 2 → 3 << 2 = 12 → n = 22 - 12 = 10.

# Outer loop iteration 2 (n = 10, d = 3):

# cnt = 0.

# Check 10 >= 3 << 1 → 3 << 1 = 6 → 10 >= 6 true → cnt = 1.

# Check 10 >= 3 << 2 → 3 << 2 = 12 → 10 >= 12 false → stop. cnt = 1.

# Update:

# quotient += 1 << 1 → 1 << 1 = 2 → quotient = 4 + 2 = 6.

# n -= 3 << 1 → n = 10 - 6 = 4.

# Outer loop iteration 3 (n = 4, d = 3):

# cnt = 0.

# Check 4 >= 3 << 1 → 3 << 1 = 6 → 4 >= 6 false → inner loop stops with cnt = 0.

# Update:

# quotient += 1 << 0 → 1 << 0 = 1 → quotient = 6 + 1 = 7.

# n -= 3 << 0 → 3 << 0 = 3 → n = 4 - 3 = 1.

# Now n = 1, which is less than d = 3, so outer loop ends.

# quotient = 7

# check overflow: quotient == (1<<31)? No (7 ≠ 2^31).

# return sign ? quotient : -quotient → sign = true → return 7.

# So the code computes 22 / 3 = 7 (truncated toward zero) — correct.
    
    