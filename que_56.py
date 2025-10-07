# 69. Merge two sorted array

# Given two sorted arrays, merge them into a single sorted array (without using built-in sort).

# Example:

# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
# Output → [1, 2, 3, 4, 5, 6]

# 🧠 Algorithm (Two Pointer Approach)

# Since both arrays are already sorted, we can use two pointers:

# Initialize i = 0 (for arr1) and j = 0 (for arr2).

# Compare arr1[i] and arr2[j].

# If arr1[i] < arr2[j], append arr1[i] to result and move i += 1.

# Else append arr2[j] and move j += 1.

# When one array ends, append the remaining elements of the other array.

# Done — the result will be sorted.

def merge_sort_array(arr1, arr2):
    i = 0
    j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:   #arr[i] > arr[j]
            merged.append(arr2[j])
            j += 1
        
    merged.extend(arr1[i:])  
    merged.extend(arr2[j:])
    
    return merged

print(merge_sort_array([1, 3, 5], [2, 4, 6]))
#what is extend()

# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)
# Output: [1, 2, 3, 4, 5, 6]