# A-3: Second-Maximum Difference in Array
# Problem:
# Find the 2nd largest absolute difference between any two numbers in the array.
# Logic:
# Find all differences using nested loops.
# Store absolute differences in a list.
# Sort and get the second largest.
#input: arr = [14, 12, 70, 15, 95, 65, 22, 30]
#first-max-difference: 95 - 12 = 83
#second-max-difference: 95 - 14 = 81
#output = 81


#O(n)
def secondMaxDifference(arr):
    if len(arr) < 2:
        print("Not Enough Elemnts")
        return
    
    max1 = max2 = float("-inf")
    min1 = min2 = float("inf")
    for num in arr:
        #for 1st and 2nd max element
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        #for 1st and 2nd min element
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    diff1 = abs(max1 - min1)
    diff2 = abs(max2 - min1)
    diff3 = abs(max1 - min2)

    diffs = sorted({diff1, diff2, diff3}, reverse=True)
    if len(diffs) < 2:
        print("Not enough unique differences")
    else:
        print("second-max-diff:", diffs[1])

secondMaxDifference([14, 12, 70, 15, 95, 65, 22, 30])
secondMaxDifference([1, 5, 9, 12])
    


print("___________")
#O(n^2)
def secondMaxDiffernce(arr):
    diff = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff.append(abs(arr[i] - arr[j]))
    diff = list(set(diff))
    diff.sort(reverse=True)

    if len(diff) < 2:
        print("Not enough unique differences")
    else:
        print("second-max-diff:", diff[1])

secondMaxDiffernce([14, 12, 70, 15, 95, 65, 22, 30])
secondMaxDiffernce([1, 5, 9, 12])