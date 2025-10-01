# 36. Find second smallest number in a given array.

def secondSmallest(arr):
    first = float("inf")
    second = float("inf")
    for i in arr:
        if i < first:
            second = first
            first = i
        elif i < second and i != first:
            second = i

    if second != float("inf"):
        return second
    else:
        return None

print(secondSmallest([5,3,9,1,6]))
print(secondSmallest([1,2,3,4]))     
print(secondSmallest([7,7,7]))


#  Find second biggest number in a given array.
print("second biigest:")

def secondBiggest(arr):
    max_element = float("-inf")
    second_max = float("-inf")
    for i in arr:
        if i > max_element:
            second_max = max_element
            max_element = i
        elif i > second_max and i != max_element:
            second_max = i
    
    if second_max != float("-inf"):
        return second_max
    else:
        return None
    
print(secondBiggest([5,3,9,1,6]))
print(secondBiggest([1,2,3,4]))     
print(secondBiggest([7,7,7]))