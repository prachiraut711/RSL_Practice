# 39.find repeating numbers in an array

#USING HASH MAP
def repeatingNum(arr):
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    temp = []
    for i, j in freq.items():
        if j > 1:
            temp.append(i)
    return temp

print(repeatingNum([1,2,3,4,4,2]))

#Set-based, order-preserving (report duplicates in the order they first repeated)
def repeatingNum(arr):
    seen = set()
    repeats = []
    for i in arr:
        if i in seen:
            if i not in repeats:
                repeats.append(i)
        else:
            seen.add(i)
    return repeats
print(repeatingNum([1,2,3,4,4,2]))
