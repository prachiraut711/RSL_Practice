# print numbers 100 to 500 and print cool if number is multiplication of 5 and print dude if number is inmultiplication of 11 and 
# print cool dude if number is in multiplication of both 5 and 11

for num in range(100, 501):
    if num % 5 == 0 and num % 11 == 0:
        print(f"{num} cool dude")
    elif num % 5 == 0:
        print(f"{num} Cool")
    elif num % 11 == 0:
        print(f"{num} Dude")