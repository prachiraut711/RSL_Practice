# 🅐 Check if digits of an integer are in ascending, descending, or not specified order
# ✅ Example
# 1378 → Ascending
# 743 → Descending
# 3574 → No specific order

# Logic
# Convert number to string (to access digits).
# Compare each digit with the next one:
# If all digits increase → Ascending
# If all digits decrease → Descending
# Otherwise → No specific order

def check_order(num):
    s = str(num)
    asc = True
    desc = True
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            desc = False
        elif s[i] > s[i + 1]:
            asc = False

    if asc:
        return "ascending"
    elif desc:
        return "Decending"
    else:
        return "No specific order"
    
print(check_order(1378))  ## Ascending
print(check_order(743))   # Decending
print(check_order(3574))  #No specific order