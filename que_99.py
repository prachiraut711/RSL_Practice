# A-2: Replace Alternate Words
# Problem:
# Given a dot-separated string like "i.like.this.program", replace every 2nd, 4th, etc. word with "xyz" without using split() or replace().
# Logic:
# Iterate manually.
# Build each word character by character.
# When a dot (.) or end of string is reached, decide whether to print the word or “xyz”.\

def replaceAlternateWords(s):
    word = ""
    count = 1

    i = 0
    while i < len(s):
        if s[i] != ".":
            word += s[i]
        if s[i] == "." or i == len(s) - 1:
            if count % 2 == 0:
                print("xyz", end="")
            else:
                print(word, end="")
            word = ""
            count += 1
            if i < len(s) - 1:
                print(".", end="")
        i += 1
replaceAlternateWords("i.like.this.program")