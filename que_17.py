#25. word wrap code.(leetcode text justify problem)

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


def testJustify(words, max_width):
    result = []
    line_words = []
    line_len = 0
    for word in words:
        if line_len + len(word) + len(line_words) > max_width:
            spaces = max_width - line_len
            if len(line_words) == 1:
                result.append(line_words[0] + " " * spaces)
            else:
                space_between = spaces // (len(line_words) - 1)
                extra = spaces % (len(line_words) - 1)
                line = ""
                for i in range(len(line_words)):
                    line += " " + line_words[i]
                    if i < len(line_words) - 1:
                        line += " " * (space_between + (1 if i < extra else 0))
                result.append(line)

            line_words = []
            line_len = 0

        line_words.append(word)
        line_len += len(word)
    
    last_line = " ".join(line_words)
    last_line += " " * (max_width - len(last_line))
    result.append(last_line)

    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16
print(testJustify(words, max_width))

# Walkthrough Line by Line
# Initialization
# result = []         # stores final justified lines
# line_words = []     # stores words in current line
# line_len = 0        # total letters (not spaces) in current line


# Start with empty result, no words in line_words, and length 0.

# Loop Begins
# Word "This"
# if line_len + len("This") + len(line_words) > 16


# 0 + 4 + 0 = 4 ≤ 16 → fits

# Add word: line_words = ["This"], line_len = 4.

# Word "is"

# Check: 4 + 2 + 1 = 7 ≤ 16 → fits

# Add: line_words = ["This","is"], line_len = 6.

# Word "an"

# Check: 6 + 2 + 2 = 10 ≤ 16 → fits

# Add: line_words = ["This","is","an"], line_len = 8.

# Word "example"

# Check: 8 + 7 + 3 = 18 > 16 → doesn’t fit

# 👉 Time to justify line "This is an"

# spaces = maxWidth - line_len = 16 - 8 = 8


# We need to distribute 8 spaces.

# space_between = 8 // (3-1) = 8 // 2 = 4
# extra = 8 % 2 = 0


# 4 spaces between each pair.

# line = "This" + " " * 4 + "is" + " " * 4 + "an"


# "This is an"

# Append to result → result = ["This is an"].

# Reset:

# line_words = []
# line_len = 0


# Add "example" → line_words = ["example"], line_len = 7.

# Word "of"

# Check: 7 + 2 + 1 = 10 ≤ 16 → fits

# Add: line_words = ["example","of"], line_len = 9.

# Word "text"

# Check: 9 + 4 + 2 = 15 ≤ 16 → fits

# Add: line_words = ["example","of","text"], line_len = 13.

# Word "justification."

# Check: 13 + 14 + 3 = 30 > 16 → doesn’t fit

# 👉 Justify "example of text"

# spaces = 16 - 13 = 3
# space_between = 3 // (3-1) = 1
# extra = 3 % 2 = 1


# Each gap has 1 space, first gap gets 1 extra.

# "example" + " " * 2 + "of" + " " * 1 + "text"


# "example of text"

# Append → result = ["This is an", "example of text"].

# Reset, add "justification.":
# line_words = ["justification."], line_len = 14.

# After Loop – Last Line
# last_line = " ".join(line_words)  # "justification."
# last_line += " " * (16 - 14)  # add 2 spaces


# "justification. "

# Append → result = ["This is an", "example of text", "justification. "].

# ✅ Final Output
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]


# Would you like me to also draw a spacing diagram for the first line "This is an" showing word positions and spaces, so it’s easier to visualize the justification?

# You said:
# explain each step  espescially this line = ""
#                 for i in range(len(line_words)):
#                     line += line_words[i]
#                     if i < len(line_words) - 1:
#                         line += " " * (space_between + (1 if i < extra else 0))
#                 result.append(line)
# ChatGPT said:
# Thought for 11s

# Nice — let’s zoom in on that exact block and unpack every detail, using the first example so it’s concrete.

# The code you asked about
# line = ""
# for i in range(len(line_words)):
#     line += line_words[i]
#     if i < len(line_words) - 1:
#         line += " " * (space_between + (1 if i < extra else 0))
# result.append(line)

# What the variables mean (right before this block runs)

# line_words — list of words collected for this line.
# Example (first line): ["This", "is", "an"].

# line_len — total number of characters in those words (no spaces). For ["This","is","an"] → 4 + 2 + 2 = 8.

# spaces = maxWidth - line_len — total spaces we must add to reach maxWidth. For maxWidth=16 → spaces = 16 - 8 = 8.

# space_between = spaces // (len(line_words)-1) — base spaces to put in each gap. Here 8 // 2 = 4.

# extra = spaces % (len(line_words)-1) — leftover spaces that must be distributed to the leftmost gaps. Here 8 % 2 = 0.

# So before the loop we have:

# line_words = ["This","is","an"]

# space_between = 4

# extra = 0

# Step-by-step iteration (first example)

# Start: line = "".

# i = 0

# line += line_words[0] → line = "This"

# i < len(line_words)-1? → 0 < 2 → True, so we add spaces:

# amount = space_between + (1 if i < extra else 0)

# = 4 + (1 if 0 < 0 else 0) = 4 + 0 = 4

# line += " " * 4 → line = "This " (4 spaces after This)

# i = 1

# line += line_words[1] → line = "This is"

# i < len(line_words)-1? → 1 < 2 → True

# amount = 4 + (1 if 1 < 0 else 0) = 4

# line += " " * 4 → line = "This is "

# i = 2

# line += line_words[2] → line = "This is an"

# i < len(line_words)-1? → 2 < 2 → False → do not add spaces after the last word.

# After the loop, result.append(line) adds "This is an" to the result.

# Key points shown by this trace

# Spaces are only added between words, never after the last word (that’s why we check i < len(line_words)-1).

# space_between is the base number of spaces for every gap.

# extra leftover spaces (if any) are given to the leftmost gaps by the (1 if i < extra else 0) term.

# Example where extra > 0 (to illustrate the (1 if i < extra else 0) behavior)

# Suppose we need spaces = 3 with 2 gaps (3 // 2 = 1, 3 % 2 = 1) — this happens for ["example","of","text"]:

# space_between = 1, extra = 1.

# Gaps become: first gap = 1 + 1 = 2 spaces, second gap = 1 + 0 = 1 space.

# Iteration:

# i=0 → add "example", then add 2 spaces → "example "

# i=1 → add "of", then add 1 space → "example of "

# i=2 → add "text", no trailing spaces → "example of text"

# This is how the algorithm ensures leftmost gaps get the extra spaces.





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