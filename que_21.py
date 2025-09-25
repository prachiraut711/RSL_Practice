# 22. print repeating elements in array in same sequence but in time complexityO(n)
# and space complexity O(1)

# We are asked:

# 👉 Given an array, find and print repeating elements.
# 👉 The repeating elements must appear in the same sequence as they first appear.
# 👉 The algorithm should work in O(n) time and O(1) extra space.

# 🔹 Example
# Input: [1, 2, 3, 1, 3, 6, 6]
# Output: 1 3 6


# Explanation:

# 1 is repeated (appears at index 0 and 3).

# 3 is repeated (appears at index 2 and 4).

# 6 is repeated (appears at index 5 and 6).
# So we print them in the order they first appear: 1, 3, 6.


# 🔹 The Challenge

# Normally, we use:

# A hash set to store visited elements → O(n) time, O(n) space ❌ (not allowed).

# We want O(1) space → so we must somehow mark elements inside the array itself.

# arr = [1, 2, 3, 1, 3, 6, 6]
# freq = {}
# for i in arr:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1

# print(freq)
# res = []
# for i, j in freq.items():
#     if j > 1:
#         res.append(i)
# print(res)

#so i cant use above dict method because it have O(n) time complexity but bcz of n no.are store in dict so the space complexity become O(n)  and we want O(1)


def printReapeating(arr):
    for i in range(len(arr)):
        x = abs(arr[i])
        if arr[x] >= 0:
            arr[x] = -arr[x]
        else:
            print(x, end =" ")

printReapeating([1, 2, 3, 1, 3, 6, 6])   #already print in function so only call the function not print it if the function was return something then only print the function