# 60.there are two clocks one is working properly(c1) and other one is dis-function(c2).
# we given c2 is x mins faster than c1 per hour. And after k mins in c1. 
# If we stop c2 clock what will be total angle between hour and min hand in c2.
# ex x=30 & k=90
# output :- 744


def nearest_angles(x, k):
    # x: minutes faster per 60 real minutes
    # k: minutes elapsed on real clock c1
    r = 1 + x/60.0
    t2 = k * r   # minutes shown on c2
    # Instantaneous angles
    minute_angle = 6 * (t2 % 60)           # angle of minute hand (0..360)
    hour_angle = 0.5 * t2                  # absolute hour-hand angle since 12:00
    diff = abs(minute_angle - hour_angle)
    smallest = min(diff, 360 - diff)       # usual clock angle (0..180)
    # Total rotations (not modulo)
    minute_total = 6 * t2
    hour_total = 0.5 * t2
    total_diff = abs(minute_total - hour_total)
    total_sum = minute_total + hour_total

    return {
        't2_minutes': t2,
        'instant_minute_angle': minute_angle,
        'instant_hour_angle': hour_angle,
        'instant_smallest_angle': smallest,
        'total_minute_rotation': minute_total,
        'total_hour_rotation': hour_total,
        'total_rotation_difference': total_diff,
        'total_rotation_sum': total_sum,
        'total_diff_rounded_int': round(total_diff),
        'total_diff_ceil': int(total_diff + 0.999999),
        'total_diff_floor': int(total_diff),
    }

# Example:
print(nearest_angles(30, 90))
# Good — this problem wording is a bit ambiguous so I’ll show the most reasonable interpretations, give formulas, compute the values for your example x = 30, k = 90, and provide a tiny Python function you can run that returns all variants so you can pick which one matches the expected 744.

# Problem restatement (one clear model)

# c1 = a correct clock. k = minutes elapsed on c1 (real elapsed time).

# c2 = the defective clock which runs faster: it gains x minutes per hour of real time (i.e. per 60 minutes of c1).

# So in 60 real minutes c2 advances 60 + x minutes on its dial.

# Rate multiplier:

# 𝑟
# =
# 60
# +
# 𝑥
# 60
# =
# 1
# +
# 𝑥
# 60
# .
# r=
# 60
# 60+x
# 	​

# =1+
# 60
# x
# 	​

# .

# After k minutes real time, the time shown on c2 (in minutes) is:

# 𝑡
# 2
# =
# 𝑘
# ⋅
# 𝑟
# t
# 2
# 	​

# =k⋅r

# (e.g. for x=30, k=90: 
# 𝑟
# =
# 1.5
# ,
#  
# 𝑡
# 2
# =
# 90
# ⋅
# 1.5
# =
# 135
# r=1.5, t
# 2
# 	​

# =90⋅1.5=135 minutes → 2:15 on c2).

# Now what could “total angle between hour and minute hand in c2” mean? I show three natural interpretations and compute each.

# Interpretation A — Instantaneous (usual) angle between the hands at the stopped time

# Compute the (smallest) angle between hour and minute hands at the time shown on c2 (standard clock angle).

# Formulas (for time t minutes since 12:00):

# minute hand angle from 12: 
# 𝜃
# 𝑚
# =
# 6
# ×
# (
# 𝑡
#  
# m
# o
# d
#  
# 60
# )
# θ
# m
# 	​

# =6×(tmod60) degrees.

# hour hand angle from 12: 
# 𝜃
# ℎ
# =
# 0.5
# ×
# 𝑡
# θ
# h
# 	​

# =0.5×t degrees.
# Then the (smallest) angle between them:

# Δ
# =
# min
# ⁡
# (
# ∣
# 𝜃
# 𝑚
# −
# 𝜃
# ℎ
# ∣
# ,
#  
# 360
# −
# ∣
# 𝜃
# 𝑚
# −
# 𝜃
# ℎ
# ∣
# )
# Δ=min(∣θ
# m
# 	​

# −θ
# h
# 	​

# ∣, 360−∣θ
# m
# 	​

# −θ
# h
# 	​

# ∣)

# For x=30, k=90:

# 𝑡
# 2
# =
# 135
# t
# 2
# 	​

# =135 min → minute angle 
# =
# 6
# ×
# 15
# =
# 90
# ∘
# =6×15=90
# ∘
# , hour angle 
# =
# 0.5
# ×
# 135
# =
# 67.5
# ∘
# =0.5×135=67.5
# ∘
# .

# Difference = 
# ∣
# 90
# −
# 67.5
# ∣
# =
# 22.5
# ∘
# ∣90−67.5∣=22.5
# ∘
# .

# So Interpretation A → 22.5°.

# Interpretation B — Absolute difference of the total degrees rotated by minute and hour hands (not modulo 360)

# This treats the two hands’ total rotation since 12:00 and returns the absolute difference (so it can exceed 360).

# Formulas (total rotation since 12:00):

# total minute hand rotation = 
# 6
# ×
# 𝑡
# 2
# 6×t
# 2
# 	​

#  degrees.

# total hour hand rotation = 
# 0.5
# ×
# 𝑡
# 2
# 0.5×t
# 2
# 	​

#  degrees.

# absolute difference = 
# ∣
# 6
# 𝑡
# 2
# −
# 0.5
# 𝑡
# 2
# ∣
# =
# 5.5
#  
# 𝑡
# 2
# ∣6t
# 2
# 	​

# −0.5t
# 2
# 	​

# ∣=5.5t
# 2
# 	​

#  degrees.

# For x=30, k=90:

# 𝑡
# 2
# =
# 135
# t
# 2
# 	​

# =135 → difference = 
# 5.5
# ×
# 135
# =
# 742.5
# ∘
# 5.5×135=742.5
# ∘
# .

# So Interpretation B → 742.5°.

# Interpretation C — Sum of the absolute angles of the two hands from 12:00

# (total degrees rotated by minute hand plus total degrees rotated by hour hand)

# value = 
# 6
# 𝑡
# 2
# +
# 0.5
# 𝑡
# 2
# =
# 6.5
# 𝑡
# 2
# 6t
# 2
# 	​

# +0.5t
# 2
# 	​

# =6.5t
# 2
# 	​

# .

# For x=30, k=90:

# 6.5
# ×
# 135
# =
# 877.5
# ∘
# 6.5×135=877.5
# ∘
# .

# So Interpretation C → 877.5°.

# Why your example says 744 (possible causes)

# None of the mathematically natural values above equals exactly 744. The closest is Interpretation B = 742.5.

# 744 could be:

# a rounding / integer-handling discrepancy (e.g. rounding 742.5 up to 744 incorrectly), or

# a small typo in the problem statement, or

# a different interpretation (for example using slightly different rate model or integer-truncation of t2).

# If the expected answer is 744, the most likely intended value was the Interpretation B (total-rotation difference) with some rounding (742.5 rounded up to 744 — though that’s an unusual rounding). Before assuming that, please tell me whether you want:

# the instantaneous smallest angle (22.5°), or

# the total-rotation difference (742.5°), or

# the sum of rotations (877.5°), or

# some integer-rounded variant.