# Remove vowels from string

def removeVowel(str):
    vowel = ["a", "e", "i", "o", "u"]
    result = ""
    for i in str:
        if i.lower() not in vowel:
            result += i
    return result

print(removeVowel("Apple"))

# If they ask for alternatives, mention:
# 1. Using a set for efficiency,
# 2. Doing it without built-ins,

def removeVowel(str):
    vowel = set("aeiouAEIOU")
    result = ""
    for i in str:
        if i not in vowel:
            result += i
    return result

print(removeVowel("Prachi"))


# without built-ins
def removeVowel(str):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for i in str:
        is_vowel = False
        for v in vowel:
            if i == v:
                is_vowel = True
                break
        if not is_vowel:
            result += i
    return result

print(removeVowel("candel"))

# dry run with "candel"
# start: result = ""
# i = 'c' → check list → not found → is_vowel=False → result = "c"
# i = 'a' → found in list → is_vowel=True → skip appending
# i = 'n' → not found → result = "cn"
# i = 'd' → not found → result = "cnd"
# i = 'e' → found → skip
# i = 'l' → not found → result = "cndl"
# return "cndl"