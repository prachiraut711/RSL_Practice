# We need to sort a binary array (only 0s and 1s) — without using another array and without using any sorting algorithm like bubble sort, quicksort, etc.

# Idea (Counting Method)
# Since the array has only 0s and 1s, we can just:
# Count the number of 0s.
# Put that many 0s in the beginning of the same array.
# Fill the rest with 1s.
# ✅ No extra array
# ✅ No sorting algorithm
# ✅ Time complexity: O(n)
# ✅ Space complexity: O(1)

 #(Counting Method)
def sort_binary_array1(arr):
    countOfZer0 = 0
    for i in arr:
        if i == 0:
            countOfZer0 += 1
    
    for i in range(len(arr)):
        if i < countOfZer0:
            arr[i] = 0
        else:
            arr[i] = 1
    return arr
arr = [1, 0, 1, 0, 1, 0, 0, 1]
print(sort_binary_array1(arr))

# Alternative: Two-pointer method (no counting)
print("___")
def sorting_binary_array2(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1

arr = [1, 0, 1, 0, 1, 0, 0, 1]
print(sorting_binary_array2(arr))


#if the question says  We need to sort a binary array (only 0s and 1s) — with “using array or any sorting algorithm”, then we have use any sorting algo
print("__")
#Using Counting + New Array
def sort_binary_array(arr):
    zeros = []
    ones = []
    for i in arr:
        if i == 0:
            zeros.append(i)
        else:
            ones.append(i)
    return zeros + ones

arr = [1, 0, 1, 0, 1, 0, 0, 1]
print(sort_binary_array(arr))

#Using Bubble Sort
print("__")
def sort_binary_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [1, 0, 1, 0, 1, 0, 0, 1]
print(sort_binary_arr(arr))