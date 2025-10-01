# # 41.find two consecutive no in array which have maximum sum

# Given an array arr of numbers, find the pair of adjacent (consecutive) elements whose sum is largest.
#  Return the maximum sum and which two numbers (and their starting index). If the array has fewer than two elements,
#  return None (no pair exists). If there are ties, the implementations below return the first pair with the maximum sum.

def max_consecutive_pair(arr):
    if len(arr) < 2:
        return None
    max_sum = arr[0] + arr[1]
    for i in range(1, len(arr) - 1): #ithe already o index cha max_sum madhhe arr[0]+arr[1]kel ata [1]+[2]as pudh karychay mahnun range 1 pasun getli ani ata last la len(arr)-1 kel bcz jr last paryant getli tar out of index hoil na plus karychay tar
        current_sum = arr[i] + arr[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

print(max_consecutive_pair([1,3,5,2,8,0,9]))

