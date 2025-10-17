# print serial like 50 51 52 53 54 55 40 41 42 43 44 45.......10 11 12 13 14 15

for i in range(50, 9, -10):  #stop = 9 → means the loop will stop when i becomes less than or equal to 9 (because we’re counting down)
    for j in range(i , i + 6):
        print(j, end = " ")
    print()   #if ha print kadla tar adva yeil sequence

#After that, i - 10 becomes 0, which is less than 9, so the loop stops.