# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33

def ncr(n, r):
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result

def getRow(rowIndex):
    row = []
    for j in range(rowIndex + 1):
        row.append(ncr(rowIndex, j))
    return row

print(getRow(3))
print(getRow(2))
print(getRow(4))