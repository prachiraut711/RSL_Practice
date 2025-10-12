# A-4: Merge Two Lists Alternately
# Problem
# Input1: [1,2,3], Input2: [a,b,c,d,e]
# Output: [1,a,2,b,3,c,d,e]

# Algorithm
# Initialize an empty list merged.
# Get lengths of both lists.
# Iterate through the lists until both are exhausted:
# Append from list1 if available.
# Append from list2 if available.
# Print merged list.

def merge_alternate(list1, list2):
    merged = []
    i = 0
    j = 0
    while i < len(list1) or j < len(list2):
        if i < len(list1):
            merged.append(list1[i])
            i += 1
        
        if j < len(list2):
            merged.append(list2[j])
            j += 1
    return merged

print(merge_alternate([1,2,3], ['a','b','c']))
print(merge_alternate([1,2,3,4,5], ['a','b','c']))
print(merge_alternate([1,2,3], ['a','b','c','d','e']))