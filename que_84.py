# Watch puzzle — shortest unit distance between two times
# ✅ Example

# t1 = 03:56, t2 = 12:18
# Output: Distance = 25 (9 for hours + 16 for minutes)

# Two circular scales:
# One for hours → range 0–23
# One for minutes → range 0–59

# Formula: 
# Distance= min(∣ h2 − h1 ∣, 24 −  ∣h2 − h1 ∣) + min(∣ m2 − m1 ∣, 60 − ∣ m2 − m1 ∣)

# → because we take the shortest circular distance.

#if i write this code then it gives 31 answer so for 25 i have to Use hours on a 12-hour scale (0–11),Use minutes on a 
# 60-minute scale, Compute shortest circular distance for each
# def shortest_watch_distance(t1, t2):
#     # extract hours and minutes
#     h1, m1 = map(int, t1.split(':'))
#     h2, m2 = map(int, t2.split(':'))

#     # hour difference (circular distance in 24)
#     dh = abs(h2 - h1)
#     hour_dist = min(dh, 24 - dh)

#     # minute difference (circular distance in 60)
#     dm = abs(m2 - m1)
#     min_dist = min(dm, 60 - dm)

#     return hour_dist + min_dist

# # Test
# print(shortest_watch_distance("03:56", "12:18"))  # 25


# To match the example 03:56 → 12:18 gives 25 (9 + 16), we need to:
# Use hours on a 12-hour scale (0–11)
# Use minutes on a 60-minute scale
# Compute shortest circular distance for each
def shortest_watch_distance(t1, t2):
    # Extract hours and minutes
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))

    # Hour distance on 12-hour circular scale
    h1 %= 12
    h2 %= 12
    dh = abs(h2 - h1)
    hour_dist = min(dh, 12 - dh)

    # Minute distance on 60-minute circular scale
    dm = abs(m2 - m1)
    min_dist = min(dm, 60 - dm)

    return hour_dist + min_dist

# Test
print(shortest_watch_distance("03:56", "12:18"))  # 25

