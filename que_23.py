#23.pascal triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

def ncr(n, r):
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i   #if i use result *= (n - i + 1) will give wrong answer bcz Using // (integer division) too early will give wrong results for some nCr values because the division truncates decimals before multiplication. Notice the result * (n - i + 1) is computed first, then integer division by i.
    return result

def pascalTriangle(numRows):
    ans = []
    for row in range(1, numRows + 1):
        temp = []
        for col in range(1, row + 1):
            temp.append(ncr(row - 1, col - 1))
        ans.append(temp)
    return ans

print(pascalTriangle(numRows = 5))
print(pascalTriangle(numRows = 4))
print(pascalTriangle(numRows = 10))
