# Print numbers whose remainder is 3 when divided by 7 (exit on 0)

while True:
    n = int(input("Enter the number (0 to exit): "))

    if n == 0:
        print("exit the program")
        break

    #here ask the remander is 3 so 21% 7 == 0 gives 0 remainder not 3 try 17 , 17 % 7 gives 3 remainder
    if n % 7 == 3:
        print(f"{n} is number whose remainder is 3 when divided by 7")
    else:
        print(f"{n} is not number whose remainder is 3 when divided by 7")
        