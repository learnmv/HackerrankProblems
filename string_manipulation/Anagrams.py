# Title: Making Anagrams
# two strings are anagrams of each other
# if the strings letters can be  rearanged to form 
# the second string
# In other words both strings must contain the same exact
# letters in the same exact frequency
# 
# # encryption is dependent on the minimum number of character deletions required to make
# the two strings anagrams.

from collections import Counter

a = input("Enter the first string: ")
b = input("Enter the second string: ")

a_count = Counter(a)
b_count = Counter(b)
common = 0
for i in a_count:
    if i in b_count:
        common += min(a_count[i],b_count[i])

total_delete = len(a)+len(b)-(2*common)
print(total_delete)