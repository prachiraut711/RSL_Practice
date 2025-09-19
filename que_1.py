# 1.Find the angle between hour and minute hand when time is 3:30

def clock_angle(hour, minute):
    # Step 1: Calculate angles of hour and minute hands
    minute_angle = 6 * minute
    hour_angle = 30 * hour + 0.5 * minute
    
    # Step 2: Find the difference
    angle = abs(hour_angle - minute_angle)
    
    # Step 3: Take the smaller angle
    final_angle = min(angle, 360 - angle)
    
    return final_angle

# Example usage
print("Angle at 3:30 =", clock_angle(3, 30), "degrees")



# 🔹 Approach

# At any given time, the angle between the hour hand and minute hand of a clock can be found using this formula:

# Angle
# =
# ∣
# 11
# 2
# ×
# 𝑀
# −
# 30
# ×
# 𝐻
# ∣
# Angle=
# 	​

# 2
# 11
# 	​

# ×M−30×H
# 	​


# Where:

# 𝐻
# H = Hour

# 𝑀
# M = Minutes

# But let’s understand how it’s derived:

# Minute hand movement

# The minute hand moves 360° in 60 minutes → 6° per minute.

# So, at 
# 𝑀
# M minutes, the minute hand’s angle from 12 o’clock =

# MinuteAngle
# =
# 6
# ×
# 𝑀
# MinuteAngle=6×M

# Hour hand movement

# The hour hand moves 360° in 12 hours → 30° per hour.

# Also, the hour hand moves as minutes pass (0.5° per minute).

# So, at 
# 𝐻
# H hours and 
# 𝑀
# M minutes, the hour hand’s angle =

# HourAngle
# =
# 30
# ×
# 𝐻
# +
# 0.5
# ×
# 𝑀
# HourAngle=30×H+0.5×M

# Angle between them

# Angle
# =
# ∣
# HourAngle
# −
# MinuteAngle
# ∣
# Angle=∣HourAngle−MinuteAngle∣

# Final step
# The clock has two angles (acute & reflex). We usually take the smaller angle, so:

# FinalAngle
# =
# min
# ⁡
# (
# Angle
# ,
# 360
# −
# Angle
# )
# FinalAngle=min(Angle,360−Angle)
# 🔹 Example: Time = 3:30

# 𝐻
# =
# 3
# ,
# 𝑀
# =
# 30
# H=3,M=30

# Minute hand = 
# 6
# ×
# 30
# =
# 180
# °
# 6×30=180°

# Hour hand = 
# 30
# ×
# 3
# +
# 0.5
# ×
# 30
# =
# 90
# +
# 15
# =
# 105
# °
# 30×3+0.5×30=90+15=105°

# Difference = 
# ∣
# 105
# −
# 180
# ∣
# =
# 75
# °
# ∣105−180∣=75°

# So, Angle = 75°