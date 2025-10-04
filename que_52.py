# 70. Check whether the vowels in a string are in alphabetical order or not

def vowels_in_order(str):
    vowel = "aeiou"
    found = []
    for i in str.lower():
        if i in vowel:
            found.append(i)
    
    return found == sorted(found)

print(vowels_in_order("education"))   # False
print(vowels_in_order("aegilou"))     # True
print(vowels_in_order("AEIOU"))       # True
print(vowels_in_order("hello"))       # True (only 'e', 'o' → already in order)

#leetcode answer (https://leetcode.com/problems/sort-vowels-in-a-string/description/)
# Input: s = "lEetcOde"
# Output: "lEOtcede"
# Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
def sortVowels(s):
    vowels = "aeiouAEIOU"
    vowel_char = sorted([i for i in s if i in vowels])
    j = 0  # # pointer for sorted vowels
    result = []
    for ch in s:
        if ch in vowels:
            result.append(vowel_char[j])
            j += 1
        else:
            result.append(ch)
    
    return "".join(result)
print(sortVowels("lEetcOde"))   # lEOtcede
print(sortVowels("lYmpH"))      # lYmpH
print(sortVowels("Programming"))# Prigrammong
print(sortVowels("HELLOworld")) # HOLLewrld
print(sortVowels("aAeEiIoOuU")) # AEEIIOOUUU