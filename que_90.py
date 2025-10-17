# balance the given string paranthesis 
# input = {}}{} 
# output = {}{}{}

def balance_braces(s):
    count = 0  # count of unmatched '{'
    pairs = 0  # total pairs

    for i in s:
        if i == "{":
            count += 1
        elif i == "}":
            if count > 0:
                count -= 1
                pairs += 1
            else:
                # unmatched '}' → treat as new pair
                pairs += 1
      # remaining unmatched '{'   
    pairs += count

    return "{}" * pairs

print(balance_braces("{}}{} "))