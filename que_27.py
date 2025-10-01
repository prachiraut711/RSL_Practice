# 28.find divisible test

def divisibility(n):
    result = []
    for i in range(2, 13):
        if n % i == 0:
            result.append(i)

    if result:
        print(f"n is divisible by {result}")
    else:
        print(f"n is not divisible by any number from 2 to 12")

divisibility(120)
divisibility(68)
divisibility(121)
divisibility(1)
