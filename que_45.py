# 52.String is anagram or not with space complexity constant

# 🔹 Problem
# Two strings are anagrams if they contain the same characters with the same frequency, ignoring order.
# Example:
# "listen" and "silent" → ✅ anagrams
# "hello" and "bello" → ❌ not anagram

#but this can give O(n) if capitalo letter also in str so below other approch is more corect
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return "Not Anagram"
    
    freq1 = {}
    freq2 = {}

    for i in s1:
        if i not in freq1:
            freq1[i] = 1
        else:
            freq1[i] += 1
    
    for i in s2:
        if i not in freq2:
            freq2[i] = 1
        else:
            freq2[i] += 1

    if freq1 == freq2:
        return "Angram"
    else:
        return "Not Anagram"
    
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "bello"))    # False



#better approch
print("________________")

def is_anagram(s1, s2):
    # Step 1: Check length
    if len(s1) != len(s2):
        return False
    
    # Step 2: Initialize count array for 26 letters
    count = [0] * 26
    
    # Step 3: Count characters in s1
    for ch in s1:
        count[ord(ch) - ord('a')] += 1
    
    # Step 4: Subtract count for s2
    for ch in s2:
        count[ord(ch) - ord('a')] -= 1
    
    # Step 5: Check if all counts are zero
    for c in count:
        if c != 0:
            return False
    return True

# Examples
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "bello"))    # False
