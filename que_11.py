# First non repeating character in the given string in O(n) complexity.

def first_non_repeating_char(s):
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
        
    
print(first_non_repeating_char("abbcaccdi"))
print(first_non_repeating_char("swiss"))