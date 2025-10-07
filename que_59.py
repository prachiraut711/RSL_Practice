# 64. Given an array including alphabates & dash.move all Dash at the end 
# without changing order of alphabets. O(N)


# You are given an array (or string) that contains alphabets and dashes (‘-’).
# Move all dashes to the end, but keep the order of alphabets same.

# ✅ Example:

# Input: ['a', '-', 'b', '-', 'c', 'd', '-']
# Output: ['a', 'b', 'c', 'd', '-', '-', '-']

# 💡 Algorithm (O(N)):

# Initialize an empty list result.

# Count how many dashes are in the array.

# Append only the alphabets first (ignoring dashes).

# Then append that many dashes at the end.

# Done

def move_dashes(arr):
    dash_count = 0
    result = []
    for i in arr:
        if i == "-":
            dash_count += 1
        else:
            result.append(i)
    
    result.extend(["-"] * dash_count)   # just extend, don’t return it
    return result  # return the final list

print(move_dashes(['a', '-', 'b', '-', 'c', 'd', '-']))