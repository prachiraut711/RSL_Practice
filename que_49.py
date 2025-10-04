# 57. Find rank of students besed on marks there was given marks of 10 students
# Suppose marks of 10 students: [50, 80, 70, 90, 60, 90, 85, 75, 65, 55]
# We want to assign ranks:
# Higher marks → better rank (smaller number).
# If two students have the same marks, they get the same rank (competition ranking).

def rank_of_students(marks):
    n = len(marks)
    sorted_marks = sorted(enumerate(marks), key= lambda x: -x[1])  # enumerate kel pahile marks array la then index ani mark ni sorted kel mahnje index pn yeil tya mark cha

    ranks = [0] * n
    rank = 1

    for i, (idx, mark) in enumerate(sorted_marks):  #[(3,90),...] ashi list yeil tyala parat enumerate kel 
        if i > 0 and mark == sorted_marks[i-1][1]:  #ithe previous mark barobar curr mark same ahe ka bagitl jar same asta tar tar previous cha 1th index gelta asta ani rank[to index] kel mahnje same rank yeil same element chi
            ranks[idx] = ranks[sorted_marks[i-1][0]]
        else:
            ranks[idx] = rank
        
        rank += 1
    
    return ranks

marks = [50, 80, 70, 90, 60, 90, 85, 75, 65, 55]
print("Marks:", marks)
print("Ranks:", rank_of_students(marks))


# What each line does (plain-language)

# n = len(marks)

# n becomes 10 (we have 10 students).

# sorted_marks = sorted(enumerate(marks), key=lambda x: -x[1])

# enumerate(marks) produces pairs (index, mark) -> [(0,50),(1,80),...,(9,55)].

# sorted(..., key=lambda x: -x[1]) sorts those pairs by the mark in descending order (because of the -x[1]).

# Result (sorted_marks) is:

# [(3, 90), (5, 90), (6, 85), (1, 80), (7, 75),
#  (2, 70), (8, 65), (4, 60), (9, 55), (0, 50)]


# Each pair is (original_index, mark).

# ranks = [0] * n

# Initialize an output list to hold each student’s rank in original order: [0,0,0,0,0,0,0,0,0,0].

# rank = 1

# Start ranking at 1 (best score → rank 1).

# for i, (idx, mark) in enumerate(sorted_marks):

# Loop through the sorted students. i is the loop position in sorted order (0..9).

# idx is the student’s original index, mark is their score.

# if i > 0 and mark == sorted_marks[i-1][1]:

# Checks whether current student’s mark equals the previous student’s mark (tie case). i>0 ensures there's a previous element to compare.

# ranks[idx] = ranks[sorted_marks[i-1][0]]

# If tie: assign the same rank number as the previous student.

# sorted_marks[i-1][0] is the previous student’s original index; ranks[...] holds the already-assigned rank for that previous student.

# else: ranks[idx] = rank

# If not a tie: assign the current rank value to this student (at their original index).

# rank += 1

# After assigning a rank to this sorted position, increment rank for the next iteration.

# Important: rank is incremented for every sorted position even when there was a tie — that makes this competition ranking (if two students share rank 1, the next gets rank 3).

# return ranks

# At the end, return ranks arranged in the original student order.