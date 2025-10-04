# 59. given list of students marks in decreasing order(same marks has same rank 
# i.e 36 34 34 20 19 1 2 2 3 4).Given new student mark. 
# find rank of new student in given list.

def find_new_student_rank(marks, new_mark):
    rank = 1
    prev_mark = None
    
    for mark in marks:
        # only update rank when mark changes
        if prev_mark is None or mark != prev_mark:
            curr_rank = rank
        prev_mark = mark
        
        # if new mark is >= current mark, return rank
        if new_mark >= mark:
            return rank
        rank += 1
        
    # if new_mark is smaller than all existing marks
    return rank

marks = [36, 34, 34, 20, 19, 4, 3, 2, 2, 1]
print(find_new_student_rank(marks, 34))  # ➝ 2
print(find_new_student_rank(marks, 35))  # ➝ 2
print(find_new_student_rank(marks, 19))  # ➝ 5
print(find_new_student_rank(marks, 0))   # ➝ 11
print(find_new_student_rank(marks, 40))  # ➝ 1