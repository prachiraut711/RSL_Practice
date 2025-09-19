# 10.Insert %20 instead of space
s = "I am prachi"
result = ""
for i in s:
    if i != " ":
        result += i 
    else:
        result += "%20"
print(result)