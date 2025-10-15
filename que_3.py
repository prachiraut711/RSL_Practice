# 3.Given array contain 1 and 0, put all 1 on left side and 0 on right side of the array

def func(arr):
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr

print(func([1, 0, 0 , 1, 1, 0]))
