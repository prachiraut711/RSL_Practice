# 44.meeting room problem.

# You are given an array of meeting time intervals intervals, where each interval is of the form [start, end].
# Determine if a person can attend all the meetings without any overlap.
# Return true if none of the intervals overlap (i.e. it’s possible to attend all meetings).
# Return false if there is at least one overlap.
# Meetings that end exactly when another starts are not considered overlapping.
# Examples of overlapping:
# [0, 30] and [5, 10] overlap → since 5 < 30
# [0, 30] and [30, 40] do not overlap → because one ends at exactly 30 and the other starts at 30

# From LeetCode:
# Each interval is a pair [start_i, end_i].
# Return true if a person could attend all meetings. — (from problem statement) 

#Solution Idea (Optimal)
# Sort the intervals by their start time.
# Iterate through the sorted intervals and for each, check if its start is less than the end of the previous interval.
# If yes → overlap → return false
# If no → continue
# If you finish without finding an overlap → return true
# Why this works:
# Once sorted by start times, any overlap must occur with adjacent intervals, not far ones.

# Examples
# intervals = [[0, 30], [5, 10], [15, 20]] → After sort: [[0,30],[5,10],[15,20]] → 5 < 30 → overlap → False
# intervals = [[7,10],[2,4]] → After sort: [[2,4],[7,10]] → 7 ≥ 4 → no overlap → True

def canAttendMeetings(intervals):
    # Step 1: Sort by start time
    intervals.sort(key=lambda x:x[0])
    
    # Step 2: Check for overlap
    for i in range(1, len(intervals)):
        # If the start of current interval is before the end of the previous => overlap
        if intervals[i][0] <= intervals[i - 1][1]:
            return False
    return True

print(canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  #false
print(canAttendMeetings([[7,10],[2,4]]))    #true

