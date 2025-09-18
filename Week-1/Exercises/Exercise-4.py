################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")
print(sum(dct.values()))

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")
max_key = max(dct, key=dct.get)
print(max_key)

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")
squared_dict = {key: value**2 for key, value in dct.items()}
print(squared_dict)

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")
even_keys = [key for key, value in dct.items() if value % 2 == 0]
print(even_keys)

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")
swapped_dict = {value: key for key, value in dct.items()}
print(swapped_dict)

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'

print("Exercise 4.6")
letter_count = {}
for char in s:
    letter_count[char] = letter_count.get(char, 0) + 1
print(letter_count)

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")
word_list = [responses_mapping[char] for char in responses]
print(word_list)

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")
animal_dict = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_keys_dict = {key: animal_dict[key] for key in sorted(animal_dict.keys())}
print(sorted_keys_dict)

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")
animal_dict = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_by_value = dict(sorted(animal_dict.items(), key=lambda item: item[1]))
print(sorted_by_value)

print("---")