# 45.implement inbuilt python functions

# 1. Implement len()
def my_len(s):
    count = 0
    for _ in s:
        count += 1
    return count

print(my_len("Hello"))  # 5

# 2. Implement max()
def my_max(lst):
    if not lst:
        return None
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum

print(my_max([1, 3, 7, 2, 5]))  # 7

# 3. Implement min()
def my_min(lst):
    if not lst:
        return None
    minimum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
    return minimum

print(my_min([1, 3, 7, 2, 5]))  # 1

# 4. Implement sum()
def my_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

print(my_sum([1, 2, 3, 4]))  # 10

# 5. Implement sorted()
# (using Bubble Sort for simplicity)

def my_sorted(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(my_sorted([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]

# 6. Implement reverse()
def my_reverse(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

# print(my_reverse("Hello"))  # "olleH"
# For your practice, I suggest you try implementing:

# count() (like "hello".count("l"))

# find() (like "hello".find("lo"))

# replace()