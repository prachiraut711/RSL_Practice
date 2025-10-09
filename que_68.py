# Problem Summary:
# You are given an array of meeting time intervals intervals[i] = [start_i, end_i].
# Return the minimum number of conference rooms required.
# Example:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Explanation:
# Meeting 1: [0, 30]
# Meeting 2: [5, 10]
# Meeting 3: [15, 20]
# Meeting 2 and 3 overlap with Meeting 1, so we need 2 rooms.
# Intuition:
# We need to know how many meetings are happening at the same time.
# The trick is to:
# Sort the start times and end times separately.
# Use two pointers to count overlapping meetings.
# Let’s carefully analyze your intervals:
#for this example below
# intervals = [[7,10], [2,4]]


# Meeting 1: 2 → 4

# Meeting 2: 7 → 10

# Step 1: Check for overlap

# Meeting 1 ends at 4

# Meeting 2 starts at 7

# ✅ There is no overlap because 7 > 4.

# Step 2: Minimum rooms needed

# Meeting 1 can use room 1

# Meeting 2 starts after meeting 1 ends, so it can use the same room

# Conclusion

# Only 1 room is sufficient.

# Key idea:

# Two rooms are needed only if meetings overlap in time.

# In this case, the meetings are at different times, so 1 room is enough.

def minMeetingRooms(intervals):
    start_times = sorted(i[0] for i in intervals)
    end_times = sorted(i[1] for i in intervals)

    start_ptr = 0
    end_ptr = 0
    used_rooms = 0
    max_rooms = 0

    while start_ptr < len(intervals):
        if start_times[start_ptr] < end_times[end_ptr]:
            used_rooms += 1
            start_ptr += 1
        else:
            used_rooms -= 1
            end_ptr += 1
        
    max_rooms = max(max_rooms, used_rooms)
    return max_rooms

print(minMeetingRooms([[0, 30], [5, 10], [15, 20]])) #2
print(minMeetingRooms([[7,10],[2,4]]))  # Meeting 2 starts after meeting 1 ends, so it can use the same room