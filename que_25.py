# find the element at row r and column c in Pascal’s Triangle (0-indexed).


def ncr(n, r):
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result

def getElement(r, c):
    return ncr(r, c)

print(getElement(4, 2))
print(getElement(5, 3))
print(getElement(3, 1))