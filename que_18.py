# 30.Leap Year using ternary operator

def is_leap_year(year):
    return "Leap Year" if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0) else "Not Leap Year"

print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(2024))
print(is_leap_year(2023))


# 🔹 Why not just divisible by 4?

# At first glance, it feels like every year divisible by 4 should be a leap year because we add an extra day (29th Feb) every 4 years.

# 👉 But if we always did this, our calendar would slowly drift away from the Earth’s actual orbit around the Sun.

# 🔹 The real reason

# Earth’s orbit around the Sun = ~365.2422 days (not exactly 365 or 365.25).

# If we only used “divisible by 4”, we would assume 365.25 days/year.

# Difference = 365.25 − 365.2422 ≈ 0.0078 days/year (~11 minutes).

# That sounds tiny, but…

# After ~128 years → error ≈ 1 whole day!

# After ~1000 years → error ≈ 8 days!

# So calendars would drift from seasons (imagine Christmas in summer 🌞🎄).

# 🔹 Fix with 100 & 400 rules

# Divisible by 4 → Leap year (basic rule).

# Divisible by 100 → NOT a leap year (skip 3 leap years every 400 years).

# Example: 1700, 1800, 1900 are divisible by 100 → ❌ not leap years.

# This corrects for the overestimation of 365.25 days.

# Divisible by 400 → Leap year again (put one back every 400 years).

# Example: 1600, 2000, 2400 → ✅ leap years.

# This balances the calendar much closer to the true solar year.

# 🔹 Quick Check

# 1900: divisible by 100 but not 400 → ❌ not leap year.

# 2000: divisible by 400 → ✅ leap year.

# 2024: divisible by 4 but not 100 → ✅ leap year.

# 2023: not divisible by 4 → ❌ not leap year.

# ✅ So the extra rules (100 and 400) exist to keep the calendar aligned with the Earth’s orbit.
# If we only used “divisible by 4”, seasons and dates would slowly drift apart.