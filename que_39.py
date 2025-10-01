#46. backtracking and simple logic (clock angle).

def angleClock(hour, minutes):
    minute_angle = 6 * minutes
    hour_angle = 30 * hour + 0.5 * minutes

    angle = abs(hour_angle - minute_angle)
    final_angle = min(angle, 360 - angle)
    
    return final_angle

print(angleClock(hour = 12, minutes = 30))
print(angleClock(hour = 3, minutes = 30))
print(angleClock(hour = 3, minutes = 15))