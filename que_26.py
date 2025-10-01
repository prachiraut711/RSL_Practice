# 31. if input is aabbbcc .O/P should be a2b3c2.

s = "aabbbcc"
result = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

result += s[-1] + str(count)   #for last element 
print(result)




# step-by-Step Execution
# Step 0: Initialize

# compressed = "" → empty string to build output.

# count = 1 → start counting first character.

# Step 1: Loop through string

# We loop i from 1 to len(s)-1 (1 to 6 for "aabbbcc"):

# i = 1 → s[1] = 'a', s[0] = 'a'

# Characters are same → count += 1 → count = 2

# i = 2 → s[2] = 'b', s[1] = 'a'

# Characters are different →

# Add 'a' + str(2) to compressed → compressed = "a2"

# Reset count = 1 for new character 'b'

# i = 3 → s[3] = 'b', s[2] = 'b'

# Characters same → count += 1 → count = 2

# i = 4 → s[4] = 'b', s[3] = 'b'

# Characters same → count += 1 → count = 3

# i = 5 → s[5] = 'c', s[4] = 'b'

# Characters different →

# Add 'b' + str(3) to compressed → compressed = "a2b3"

# Reset count = 1 for new character 'c'

# i = 6 → s[6] = 'c', s[5] = 'c'

# Characters same → count += 1 → count = 2

# Step 2: Add last character

# After the loop, we must add the last character because it hasn’t been added yet:

# compressed += s[-1] + str(count)


# s[-1] = 'c', count = 2 → add 'c2'

# compressed = "a2b3c2" ✅