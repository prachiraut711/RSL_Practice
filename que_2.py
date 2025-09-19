# 2.If given String is I_LOVE_INDIA reverse whole string 
# except "_". Output for this would be A_IDNI_EVOLI


def reverseString(str):
    rev  = str[::-1]
    temp = []
    
    for i in range(len(rev)):
        if rev[i].isalpha():
            temp.append(rev[i])
    
    for i in range(len(str)):
        if not str[i].isalpha():
            temp.insert(i, str[i])

    return "".join(temp)

print(reverseString("I_LOVE_INDIA"))


            
