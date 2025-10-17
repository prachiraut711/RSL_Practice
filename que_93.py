#draw this pyramid pattern
# *
# ***
# *****
# *******

rows = 4
for i in range(rows):
    stars = "*" * (2 * i + 1)
    print(stars)