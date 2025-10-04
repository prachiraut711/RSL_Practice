# 68. count pairs in array map implementation

# Problem

# Given an array of integers, count all pairs (i, j) such that i < j and arr[i] == arr[j].

# Example:

# arr = [1, 2, 1, 1, 2]
# Pairs:
# (0,2) → arr[0]=1, arr[2]=1
# (0,3) → arr[0]=1, arr[3]=1
# (2,3) → arr[2]=1, arr[3]=1
# (1,4) → arr[1]=2, arr[4]=2
# Total pairs = 4

# 🧠 Algorithm (Map / Dictionary Implementation)

# Create a frequency map to count occurrences of each number in the array.

# Example: {1: 3, 2: 2}

# For each number in the map, number of pairs = freq * (freq - 1) / 2

# This comes from combinatorial formula nC2 = number of ways to pick 2 items from n.

# Sum all pairs for all numbers → final answer.

def count_pairs(arr):
    freq_map = {}
    for i in arr:
        if i not in freq_map:
            freq_map[i] = 1
        else:
            freq_map[i] += 1
    
    total_pair = 0
    for freq in freq_map.values():
        if freq > 1: # as 1 chi pair honar nahi so greater than 1 havi na pair hoyla
            total_pair += freq * (freq - 1) // 2
    return total_pair

print(count_pairs([1,2,1,1,2]))
