# 51.check whether string is cyclic or not

# ✅ Problem:
# A string is cyclic (or a rotation of itself) if by rotating its characters you can get the same string again.
# For example:
# "abc" → cyclic rotations are "abc", "bca", "cab".
# "abcd" → cyclic rotations are "abcd", "bcda", "cdab", "dabc".
# If we are given two strings, we usually check if one is a cyclic rotation of the other.
# If only one string is given, we usually check if it can be rotated into itself (which is always true).

def is_cyclic(s1, s2):
    if len(s1) != len(s2):
        return "Not Cyclic"
    
    temp = s1 + s1

    if s2 in temp:
        return "Cyclic"
    else:
        return "Not Cyclic"

print(is_cyclic("abc", "bca"))  #true
print(is_cyclic("abcd", "acbd"))  # False
print(is_cyclic("ab", "a"))  #false