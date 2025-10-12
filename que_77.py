# A-2: Reverse Words in a Dot-Separated String (Without using built-in functions)
# 🔹 Problem

# Input: "i.like.this.program.very.much"
# Output: "much.very.program.this.like.i"

# 🔹 Algorithm

# Take the string and store it in a variable s.
# Initialize an empty list words and an empty string word.
# Loop through each character:
# If the character is not ., add it to word.
# If it is ., append word to words and reset word to an empty string.
# Append the last word to words.
# Reverse the words list manually using a loop.
# Join them with . and print.

#without using built in funcion
def reverse_dot_string(str):
    stack = []
    word = ""
    for i in str:
        if i != ".":
            word += i
        else:
            stack.append(word)
            word = ""
    stack.append(word)
    
    result = ""
    first = True
    while stack:
        temp = stack.pop()
        if first:
            result += temp
            first = False
        else:
            result += "." + temp
    return result
        
print(reverse_dot_string("i.like.this.program.very.much"))

print("____")
#but this has inbuilt function question says dont use so 
def reverseWithDot(str):
    temp = []
    word = ""
    for i in str:
        if i != ".":
            word += i
        else:
            temp.append(word)
            word = ""
    
    if word:
        temp.append(word)

    return ".".join(temp[::-1])
print(reverseWithDot("i.like.this.program.very.much"))


