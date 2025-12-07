

from get_input import fetch_input

rucksacks = fetch_input(2022,3).splitlines()
# import code; code.interact(local=locals())

# Our test, set:
items = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

# General Logic to build Priorities Hash-map
lower_alpha = [chr(x) for x in range(ord('a'),ord('z')+1)]
upper_alpha = [chr(x) for x in range(ord('A'),ord('Z')+1)]

lower_dict = {v:k+1 for k,v in enumerate(lower_alpha)}
upper_dict = {v:k+27 for k,v in enumerate(upper_alpha)}

sum_prorities = 0

# Part-1 Logic

import textwrap

for rucksack in rucksacks:
    first,last = textwrap.wrap(rucksack,len(rucksack)//2) # We could've used string slicing, but Here we use the textwrap module to split a string into 2 equal parts
    for char in first:
        if char in last:
            print(char)
            if char in lower_alpha:
                sum_prorities += lower_dict[char]
            elif char in upper_alpha:
                sum_prorities += upper_dict[char]
            break
print(sum_prorities)

# Part-2 Logic
for i in range(0, len(rucksacks), 3):
    a, b, c = rucksacks[i:i+3]
    # use a, b, c here
    for char in a:
        if char in b and char in c:
            sum_prorities += lower_dict.get(char,upper_dict.get(char))  # type: ignore
            break
print(sum_prorities)