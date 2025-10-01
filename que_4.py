# 4.Check if two given Strings are anagram of each other.

# For this I gave answer to use two hashmaps and compare both, 
# he asked another approach. So I told him i can use two array with 
# length 256 and store charachter values against ASCII index and than
# compare both arrays. He asked for another So I told him we can sort 
# the array and compare both arrays. Than he asked if there is an 
# inbuilt function which we can use, I was not able to answer.


# Method 1 : use two hashmaps and compare both

def are_anagrams(s, t):

    if len(s) != len(t):
        return False
    

    dict_1 = {}
    dict_2 = {}

    for i in s:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1

    for i in t:
        if i in dict_2:
            dict_2[i] += 1
        else:
            dict_2[i] = 1
    
    if dict_1 == dict_2:
        return "IT'S ANAGRAM"
    else:
        return "NOT ANAGRAM"
    
    # return dict_1 == dict_2   if ask to compare then if this give true if anagram 


print(are_anagrams("rac", "car"))


# Method 2 :Using Two Arrays of length 256 (for ASCII characters)

def are_anagrams(s, t):
    if len(s) != len(t):
        return False
    
    freq_1 = [0] * 256
    freq_2 = [0] * 256

    for i in s:
        freq_1[ord(i)] += 1

    for i in t:
        freq_2[ord(i)] += 1

    if freq_1 == freq_2:
        return "Anagram"
    else:
        return "Not Anagram"

print(are_anagrams("race", "car"))