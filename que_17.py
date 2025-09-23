#25. word wrap code.(leetcode text justify problem)

def fullJustify(words, maxWidth):
    result = []
    line_words = []
    line_len = 0

    for word in words:
        # check if adding this word exceeds maxWidth
        if line_len + len(word) + len(line_words) > maxWidth:
            spaces = maxWidth - line_len
            if len(line_words) == 1:  # only one word
                result.append(line_words[0] + " " * spaces)
            else:
                space_between = spaces // (len(line_words) - 1)
                extra = spaces % (len(line_words) - 1)
                line = ""
                for i in range(len(line_words)):
                    line += line_words[i]
                    if i < len(line_words) - 1:
                        line += " " * (space_between + (1 if i < extra else 0))
                result.append(line)

            line_words = []
            line_len = 0

        line_words.append(word)
        line_len += len(word)

    # last line → left justify
    last_line = " ".join(line_words)
    last_line += " " * (maxWidth - len(last_line))
    result.append(last_line)

    return result





# algo:
# Split the input text into words.
# Keep adding words to the current line until adding the next word would exceed the given max_width.
# If it exceeds → push current line to result, start a new line.
# Continue until all words are placed.

def word_wrap(text, max_width):
    words = text.split()
    result = []
    line = ""
    
    for word in words:
        if len(line) + len(word) + (1 if line else 0) > max_width:
            result.append(line)
            line = word
        else:
            line += (" " if line else "") + word    # ithe in first condition jar else "" nast kel tar [' Given an array'] as al ast given chya pudhe pn space te starting la nko ahe aplyala so mag at fist line is empty mahnun ""space nahi dili at first word
    #ithe " " dilay because "" + "given" ne given_ ha underline vala space yetoy mahnun he getl
    if line:
        result.append(line)
 
    return result

text = "Given an array of strings strs, group the anagrams together"
max_width = 15
print(word_wrap(text, max_width))
    


# Step-by-step execution
# 1) Prepare words & lengths
# words = text.split() → splits on whitespace, so punctuation stays attached to a word.
# Words and lengths (each character counted):
# "Given" → 5
# "an" → 2
# "array" → 5
# "of" → 2
# "strings" → 7
# "strs," → 5 (comma is a character)
# "group" → 5
# "the" → 3
# "anagrams" → 8
# "together" → 8
# Initial variables:
# result = []
# line = "" (empty)
# 2) Iterate over words — detailed trace
# I'll show for each word: current line (before), the arithmetic check, decision, and new state.
# Word 1: "Given" (len=5)
# len(line) = 0 (line is empty)
# Compute: 0 + 5 + (0) = 5 → (0 + 5 = 5; +0 = 5)
# 5 > 15? → No → go to else branch.
# line = "" + "Given" = "Given"
# result = []
# Word 2: "an" (len=2)

# len(line) = 5 ("Given")

# Compute: 5 + 2 + 1 = 8 → (5 + 2 = 7; +1 = 8)

# 8 > 15? → No

# line = "Given" + " " + "an" = "Given an"

# result = []

# Word 3: "array" (len=5)

# len(line) = 8 ("Given an")

# Compute: 8 + 5 + 1 = 14 → (8 + 5 = 13; +1 = 14)

# 14 > 15? → No

# line = "Given an array" (length = 14)

# result = []

# Word 4: "of" (len=2)

# len(line) = 14 ("Given an array")

# Compute: 14 + 2 + 1 = 17 → (14 + 2 = 16; +1 = 17)

# 17 > 15? → Yes → wrap now.

# result.append("Given an array") → result = ["Given an array"]

# Start new line: line = "of"

# Word 5: "strings" (len=7)

# len(line) = 2 ("of")

# Compute: 2 + 7 + 1 = 10 → (2 + 7 = 9; +1 = 10)

# 10 > 15? → No

# line = "of strings" (length = 10)

# result = ["Given an array"]

# Word 6: "strs," (len=5)

# len(line) = 10 ("of strings")

# Compute: 10 + 5 + 1 = 16 → (10 + 5 = 15; +1 = 16)

# 16 > 15? → Yes → wrap.

# result.append("of strings") → result = ["Given an array", "of strings"]

# line = "strs,"

# Word 7: "group" (len=5)

# len(line) = 5 ("strs,")

# Compute: 5 + 5 + 1 = 11 → (5 + 5 = 10; +1 = 11)

# 11 > 15? → No

# line = "strs, group" (length = 11)

# result = ["Given an array", "of strings"]

# Word 8: "the" (len=3)

# len(line) = 11 ("strs, group")

# Compute: 11 + 3 + 1 = 15 → (11 + 3 = 14; +1 = 15)

# 15 > 15? → No (note: the condition uses > not >=)

# line = "strs, group the" (length = 15 exactly)

# result = ["Given an array", "of strings"]

# Word 9: "anagrams" (len=8)

# len(line) = 15 ("strs, group the")

# Compute: 15 + 8 + 1 = 24 → (15 + 8 = 23; +1 = 24)

# 24 > 15? → Yes → wrap.

# result.append("strs, group the") → result = ["Given an array", "of strings", "strs, group the"]

# line = "anagrams"

# Word 10: "together" (len=8)

# len(line) = 8 ("anagrams")

# Compute: 8 + 8 + 1 = 17 → (8 + 8 = 16; +1 = 17)

# 17 > 15? → Yes → wrap.

# result.append("anagrams") → result = ["Given an array", "of strings", "strs, group the", "anagrams"]

# line = "together"

# End of loop — there is a non-empty line ("together"), so append it:

# result.append("together")

# Final result list
# [
#   "Given an array",
#   "of strings",
#   "strs, group the",
#   "anagrams",
#   "together"
# ]