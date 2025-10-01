# 32.First non repeating number in an array

def firstNonReapetingNum(arr):
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for i in arr:
        if freq[i] == 1:
            return i
    return -1   #if no non-repeating found

# Examples
print(firstNonReapetingNum([1,1,2,3,3]))       # Output: 2
print(firstNonReapetingNum([4,5,1,2,1,2,3,5])) # Output: 4
print(firstNonReapetingNum([1,1,2,2,3,3]) )


#same for in string 
print("for string question")
# 387. First Unique Character in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

def firstUniqChar(str):
    freq = {}
    for i in str:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for i in str:
        if freq[i] == 1:
            return i
    return -1

print(firstUniqChar("prachi"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))