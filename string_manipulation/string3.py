# title: Sherlock and the valid string
# a string is valid if all characters of the string appear the same number of times
# it is also valid if he can remove just 1 character at 1 index in the string
# and remaining characters will occur the same numver of times.
from collections import Counter

s = input('enter string: ')
prev_letter = s[0]
s_count = Counter(s)
prev_value = s_count[prev_letter]
for key,value in s_count.items():
    if value == prev_value:
        continue
    elif abs(value - prev_value) > 1:
        print(False)
        break
