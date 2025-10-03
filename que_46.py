# 53.Find equilibrium point(index) in given array. Equilibrium point is 
# the element from where sum of all elements left to it is equal to sum 
# of all elements right to it.

# Example
# Input:
# arr = [1, 3, 5, 2, 2]
# Explanation:
# Index 0 → left sum = 0, right sum = 12 → not equal
# Index 1 → left sum = 1, right sum = 9 → not equal
# Index 2 → left sum = 4, right sum = 4 ✅
# So, equilibrium index = 2.

def equilibrium_index(arr):
    if len(arr) == 0:
        return -1
    #calculated total sum of array we know total_sum = left_sum + arr[i] + right_sum
    total_sum = 0
    for i in arr:
        total_sum += i

    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i
        
        left_sum += arr[i]

    return -1 # No equilibrium point found

print(equilibrium_index([1, 3, 5, 2, 2]))
print(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))
print(equilibrium_index([1,2,0,3]))
print(equilibrium_index([1, 1, 1,1]))
print(equilibrium_index([0]))
print(equilibrium_index([]))
