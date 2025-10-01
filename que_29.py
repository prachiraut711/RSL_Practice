# 34.write code to detect any binary sequence

def is_binary_sequence(s):
    for i in s:
        if i not in ("0", "1"):
            return False
    return True
    
print(is_binary_sequence("1010101"))   # True
print(is_binary_sequence("11002"))     # False
print(is_binary_sequence("0000"))      # True
print(is_binary_sequence("abc101"))    # False


# i not in ("0", "1") checks if the character is not "0" or "1".

# If it finds a character that is neither 0 nor 1, it immediately returns False.

# Example:

# For "11002", it will check '1' (ok), '1' (ok), '0' (ok), '0' (ok), '2' (not 0 or 1 → returns False immediately).