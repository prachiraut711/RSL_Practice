# ank of the newly entered mark
# ✅ Example

# Marks List = {39, 38, 38, 36, 34, 31, 28}
# If new mark = 38 → Rank 2
# If new mark = 37 → Rank 3
# If new mark = 36 → Rank 3

# 🔹 Logic

# Sort the marks in descending order.
# Remove duplicates to handle same marks (since they share the same rank).
# The rank = position (index + 1) of where the new mark fits in the sorted list.

def find_rank(marks, new_mark):
    #Sort the marks in descending order.
    marks = sorted(marks, reverse=True)
    # Remove duplicates (to handle same marks with same rank)
    unique = []
    for i in marks:
        if i not in unique:
            unique.append(i)
    
    for i in range(len(unique)):
        if new_mark >= unique[i]:
            return f"Rank{i + 1}"
     #if ne_mark is less than every element in list means last rank
    return f"Rank{len(unique) + 1}"

marks = [39, 38, 38, 36, 34, 31, 28]
print(find_rank(marks, 38))  # Rank2
print(find_rank(marks, 37))  # Rank3
print(find_rank(marks, 36))  # Rank3
