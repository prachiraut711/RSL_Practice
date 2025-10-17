# Print the sum of elements of the lower triangular matrix

# What is a Lower Triangular Matrix?
# In a square matrix, the lower triangular part includes all elements on and below the main diagonal.
# Example:
# Matrix:
# 1  2  3
# 4  5  6
# 7  8  9

# Lower triangular elements (on and below diagonal):
# 1
# 4 5
# 7 8 9
# Sum = 1 + 4 + 5 + 7 + 8 + 9 = 34

# Algorithm
# Read the matrix.
# Initialize sum = 0.
# Loop through rows i and columns j.
# Add matrix[i][j] to sum only if i >= j (i.e., below or on diagonal).
# Print the sum.

def lower_triangular_sum(mat):
    n = len(mat)
    sum = 0
    for i in range(n):
        for j in range(n):
            if i >= j:
                sum += mat[i][j]
    return sum

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("lower triangular sum: ", (lower_triangular_sum(mat)))


# simliar for upper triagular matrix sum just i <= j
def upper_triangular_sum(mat):
    n = len(mat)
    sum = 0
    for i in range(n):
        for j in range(n):
            if i <= j:
                sum += mat[i][j]
    return sum

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("upper triangular sum: ", (upper_triangular_sum(mat)))