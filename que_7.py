# 9. Program for reversing words of a given string 
# (eg. “I love my country” will be reversed as “country my love I”)

def reverse(str):
    temp = str.split()
    temp = temp[::-1]
    return " ".join(temp)

print(reverse("I love my country"))

#better approch without split
def reverse(s):
    words = []
    word = ""
    for i in s:
        if i != " ":
            word += i
        else:
            words.append(word)
            word = ""
    words.append(word)
    words = words[::-1]
    ans = " ".join(words)
    return ans

s = "I Love My Country"
print(reverse(s))
