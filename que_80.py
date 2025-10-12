# Problem Explanation

# You are given a list of integers where:

# Every element appears twice, except for one element that appears once.
# You need to find that non-duplicate number.

#O(n) time complexity O(1) space complexity(best approch)
def find_single_num(arr):
    result = 0
    for i in arr:
        result ^= i
    return result

print(find_single_num([4, 1, 2, 1, 2]))


print("____")
#O(n) time complexity O(n) space complexty
def find_single_num(arr):
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    for i, j in freq.items():
        if j == 1:
            return i
print(find_single_num([4, 1, 2, 1, 2]))
