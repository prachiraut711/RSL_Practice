# 48.Maximum Frequency Character and its frequency
def maxFrequencyChar(s):
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    max_count = 0
    max_char = ""
    for i, j in freq.items():
        if j > max_count:
            max_count = j
            max_char = i
    return max_char, max_count

print(maxFrequencyChar("Hello World"))



#This only returns the count, not the character itself. Usually, we want both the character and its frequency.
def maxFreqChar(s):
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    for i, j in freq.items():
        if j == max(freq.values()):
            return j
        
print(maxFreqChar("Hello World"))