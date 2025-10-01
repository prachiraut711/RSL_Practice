# 35.print two digit possible numbers from 0 to 5, but the two digit number should be like decreasing one's place and increasing tens place.

# Step 1: Understand the question
# Print two-digit numbers using digits from 0 to 5, such that:
# Tens digit increases
# Ones digit decreases

# Let’s denote the number as AB where:
# A = tens place
# B = ones place

# Constraints:
# 0 ≤ A ≤ 5
# 0 ≤ B ≤ 5
# Tens digit (A) < Ones digit (B)? Or decreasing ones and increasing tens? Let’s clarify:
# “Decreasing one's place” → ones digit is smaller than tens digit?
# “Increasing tens place” → tens digit increases as we go.
# So essentially, we want A > B, using digits 0–5, and print all such numbers.

# Example possibilities:

# 10 → A=1, B=0 ✅ (tens increasing, ones decreasing)

# 21 → A=2, B=1 ✅

# 50 → A=5, B=0 ✅

for tens in range(0, 6):
    for ones in range(0, 6):
        if ones < tens:
            print(f"{tens}{ones}", end = " ")
