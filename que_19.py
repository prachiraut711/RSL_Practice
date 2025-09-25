# Find the mid 4 characters of a strings

# This means:

# You are given a string (for example: "abcdefgh").

# You need to extract exactly 4 characters that are positioned in the middle of the string.

# The "middle" means the 4 characters should be centered around the middle index of the string.

# 🔹 Example 1

# Input:
# s = "abcdefgh" (length = 8)

# Middle position = between index 3 and 4.
# So the 4 middle characters are: "cdef" (indices 2,3,4,5).

# Output: "cdef"

# 🔹 Example 2

# Input:
# s = "abcdefg" (length = 7)

# Middle index = 3 (character "d").
# So the 4 middle characters are: "bcde" (indices 1,2,3,4).

# Output: "bcde"

def middleOfString(str):
    n = len(str)
    if n < 4:    #if str = "abc" or "ab" or "a" less than 4 so there will be no 4
        return "String does not have 4 charaters" 
    
    start = (len(str) - 4) // 2
    return str[start : start + 4]

print(middleOfString("abcdefgh"))  #(length = 8)
print(middleOfString("abcdefg"))  #(length = 7)
print(middleOfString("qwert")) #lenght = 5
print(middleOfString("ab"))