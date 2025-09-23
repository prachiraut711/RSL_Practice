# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]


from collections import defaultdict

def group_anagram(arr):
    anagram = defaultdict(list)   
    for i in arr:
        key = "".join(sorted(i))
        anagram[key].append(i)
    return list(anagram.values())
print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
print(group_anagram(["a"]))
print(group_anagram([""]))



# What each line does

# from collections import defaultdict

# Imports defaultdict, a dict subclass that creates a default value for missing keys automatically.

# def group_anagrams(words):

# Defines a function that takes a list of strings words.

# anagrams = defaultdict(list)

# Creates an empty mapping. When you access a key that doesn’t exist, defaultdict will create it and set its value to list() (an empty list). This saves you from checking if key not in dict before appending.

# for word in words:

# Loop over each word in the input list.

# key = "".join(sorted(word))

# sorted(word) returns a list of the characters in word sorted in lexicographic order.
# Example: sorted("eat") → ['a','e','t'].

# "".join(...) converts that list back into a string: ''.join(['a','e','t']) → "aet".

# This canonical sorted string is used as the grouping key: all anagrams produce the same key.

# anagrams[key].append(word)

# Because anagrams is a defaultdict(list), if key does not exist a new empty list is created automatically and then word is appended to that list.

# return list(anagrams.values())

# anagrams.values() is a view of all the grouped lists; wrapping with list(...) returns the list-of-lists result you want, e.g. [['eat','tea','ate'], ['tan','nat'], ['bat']].
