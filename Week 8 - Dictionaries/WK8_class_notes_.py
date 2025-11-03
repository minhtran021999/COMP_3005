# WEEK 8 - Dictionaries

###############################################
#-------------- Dictionaries -----------------#
###############################################

'''
Dictionaries are used for data consisting of a set of properties for a single item.
Lookup is accomplished using a dictionary 'key' vs indexing or iterating. It follows that dictionaries
provide faster search capability (useful for large datasets, csv files, api's) but at a cost of element selection.

Dictionaries are:
    - comprised of key value pairs, keys must be unique, hashable/immutable (ints, floats, strings, bools, frozen
        sets and tuples). There are no restrictions on values.
    - unordered --> can't be searched by "index", instead they are indexed by key(s) for faster lookup ***main difference from lists
    - capable of nested structure
    - mutable
    - heterogenous

*** lists and dictionaries cannot be used as keys because they are mutable

keys are unique (within one dictionary). If you store using a key that is already in use, the old value associated with that key is forgotten.
'''

##########################################
#-------------- Methods -----------------#
##########################################

# Review dict methods -- experiment with these on your homework 8 as you see fit.

[method for method in dir(dict) if not method.startswith('__')]

'''
clear() — Removes all items from the dictionary, leaving it empty.
copy() — Returns a shallow copy of the dictionary (a new dictionary with the same key–value pairs).
fromkeys(iterable, value=None) — Creates a new dictionary with keys from the given iterable and assigns each key the same value
get(key, default=None) — Returns the value for a given key; if the key doesn’t exist, returns the default value (instead of raising an error).
items() — Returns a view object that displays a list of the dictionary’s key–value pairs as tuples.
keys() — Returns a view object containing all the dictionary’s keys.
pop(key, default=None) — Removes the specified key and returns its value.
popitem() — Removes and returns the last inserted key–value pair as a tuple (key, value).
values() — Returns a view object containing all the dictionary’s values.
'''

########################################################
#-------------- Creating Dictionaries -----------------#
########################################################

# Seven approaches - there are more!

# Example 1a. literal syntax

d1 = {} # empty dictionary

d1 = {'Age': 57, 'Class': 1982}  # smaller datasets

# Example 1b. dict() constructor

d1 = dict(Age = 57, Class = 1982) # using keywords

# Example 1c. dict() constructor using iterable of pairs

d1 = dict([('Age', 57), ['Class', 1982]]) #any iterable with elements that are 2-element iterables

# Example 1d. dict() constructor using zip

keys = ['a', 'b', 'c', 'd']

values = [10, 20, 30, 40]

d1 = dict(zip(keys, values))

# compare 1d to the following

dict = {}
for k, v in zip(keys, values):
    dict[k] = v

# Another variation of this

keys = 'abcd'
values = range(1,5)

{k:v for k,v in zip(keys, values) if v % 2 == 0}

# Example 1e  .fromkeys() Method

k = ('a', 'b', 'c')
v = (0, 1, 2)
dict.fromkeys(k, v) # {'a': (0, 1, 2), 'b': (0, 1, 2), 'c': (0, 1, 2)}

# or

dict.fromkeys(('a', 'b', 'c'), -999)

dict.fromkeys('abc', -999)

# Note: order of keys returned may be different in Jupyter, otherwise order is maintained. print() will retain order. Always check!

# Example 1f. dictionary comprehension

{x: x**2 for x in range(1,11)} # builds programmatically

# Example 1e. using .fromkeys() method to initialize with defaults

d1 = dict.fromkeys(["name", "address", "phone_number"], None)


##############################################
#-------------- Hashability -----------------#
##############################################

# Dictionary keys must be immutable and unique -> hashable

# Example 2a.

d1 = {(1, 2, 3): 'this is a tuple'}

hash((1,2,3)) # hash takes one argument

hash(d1) # unhashable type: 'dict' (mutable)

d1 = {[1, 2, 3]: 45} # unhashable type 'list'


# Example 2b. functions are hashable

def print_args(a, b, c):
    print(a, b, c)

hash(print_args) # e.g., 269416418

# Example 2c. function use case - storing functions and arguments for subsequent use

dict_function = {print_args: [6,7,8] }

print(dict_function) # {<function nums at 0x100ef7d80>: [6, 7, 8]}

# This allows use to store functions in a dict for subsequent execution

def func_sub(a, b):
    return a - b

def func_inv(a):
    return 1/a

def func_mult(a, b):
    return a * b

# When we iterate over a dictionary we get the keys back

dict_functions = {func_sub:(3, 5), func_inv: (2, ), func_mult: (4,6)} # want func_inv to be a tuple so that it can be unpacked

print(dict_functions) # {<function func_sub at 0x100f08860>: (3, 5), <function func_inv at 0x100f08540>: (2,), <function func_mult at 0x100f089a0>: (4, 6)}

for fn in dict_functions:
    print(fn) # <function func_sub at 0x100f08860> <function func_inv at 0x100f08540> <function func_mult at 0x100f089a0> --> prints dict keys when we loop over dict

# iterate over keys (functions themselves)
for fn in dict_functions:
    result = fn(*dict_functions[fn]) # unpack values and pass to function (item)
    print(result)


##############################################
#--------- Clearing a Dictionary ------------#
##############################################

# Example 3a - reassignment
#
keys = 'abcd'
values = range(1,5)

d = {k:v for k,v in zip(keys, values)}

d = {} # doesnt clear dictionary, assigns a new dictionary to the name reference
id(d)

# Example 3b. .clear()

d = dict(zip('abc', 'def'))
id(d)
d.clear()
id(d) # mutates the dictionary in place

##############################################
#-------------- Keys:Values -----------------#
##############################################

# Example 4a. Accessing values via. key indexing

person = {"name": "John", "gender": "male"} # note colon placed after quotes

person["name"] # index to get value of name

# Example 4b. Accessing values via. key .get() method

person.get("name") # .get() method -> does not create a new key or set a default

person['age'] # this will throw a key error
person.get("age") # 'age' does not exist, .get() prevents a KeyError and returns None
person.get("age", "message") # returns "message" if age doesnt exist, does not update dictionary

# Using .get(): counting frequency of values/chars

text = 'if Char exists, get current number & add 1 to it, then store to dict under the same key'

counts = dict()

for c in text:
    counts[c] = counts.get(c, 0) + 1
# # if key doesnt exist, set count to 0 & add 1 to it, & save into the dict.
# # if Char exists, get current number & add 1 to it, then store to dict under the same key
print(counts)

# Using .get(): managing case and eliminate white space

counts = dict()
for c in text:
    key = c.lower().strip()
    if key: # if key not empty
        counts[key] = counts.get(key,0) +1
print(counts)


# Example 4c. Accessing values via. key .setdefault() method -> creates new key if absent, sets default

data = {x: x**2 for x in range(1,11)}

data.setdefault(4, 'Missing_Value') #16
data.setdefault(11, 'Missing_Value') #Missing Value

# Example 4c. Modifying Dictionaries - adding data

person['birth_year'] = '2003' # provide dict name, key in brackets = value

print(f'{person['name']} is a {person['gender']} born in {person['year']}.')

# Example 4d. updating data

person['birth_year'] = '2023' # we can update the dictionary value at the birth_year key

person.update({'gender': 'female'})

# Example 3d. deleting data using del function

try:
    del person['gender']
except:
    print('Key does not exist')

# Example 4e. Additional indexing examples

data = {'team': 'Boston Redsox', 'wins': {'2018': 108, '2017': 93}}
data['wins'] # {'2018': 108, '2017': 93}
data['wins']['2018'] # 108

nested_list = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]
nested_list[1]['c'] # 90

# Example 4f. .pop() method

data = dict(list(zip('abcde', (1, 2, 3, 4, 5))))

result = data.pop('b') # removes key:val from d and saves them to result, will get KeyError if key doesnt exist

print(result)

data = {'a':1, 'b': 2}

data.pop('a', 100) # -> returns 1, key existed

data.pop('z', 100) # -> get 100 back, dict not affected

# Example 4g. .popitem()

d.popitem() # removes last element from dictionary, returns the key:value of the element. When dictionary is empty, get keyerror.


##############################################
#-------setdefault(): in depth -------------#
##############################################

# create dictionary with list of all chars used in text, group by lowercase, uppercase, punctuation other than whitespace

text = 'if Char exists, get current number & add 1 to it, then store to Dict under the same key'

import string

print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ


# create dict with three keys (categories) with values that are chars from text that fit the categories

# categories = {}

# for c in text:
#     if c != ' ':
#         if c in string.ascii_lowercase:
#             key = 'lower'
#         elif c in string.ascii_uppercase:
#             key = 'upper'
#         else:
#             key = 'other'

#     # set value of each key to a set
#         if key not in categories:
#             categories[key] = set()

#         categories[key].add(c) # .add from set method, add char c if not present

# for cat in categories:
#     print(f'{cat}: ', ''.join(categories[cat]))


# refactor using setdefault

categories = {}

for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'

        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))

# another refactor

# def cat_key(c):
#     categories ={' ': None,
#                 string.ascii_lowercase: 'lower',
#                 string.ascii_uppercase: 'upper'}

#     for key in categories:
#         if c in key:
#             return categories[key]
#     else:
#         return 'other'

# cat_key('a') # lower
# cat_key('A') # upper
# cat_key(',') # other
# cat_key(' ') # None

# #### Chain in itertools

# from itertools import chain

# def cat_key(c):
#     cat_1 = {' ':None}
#     cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower') # every char in ascii lowercase will be key in dict, with value 'lower'
#     cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')

#     # merge dictionaries --> use chain to create an iterable of tuples containing the key: value pair

#     categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
#     # categories = {**cat_1, **cat_2, **cat_3}

#     #chars are individual keys inside categories dictionary. Can use as fast lookup
#     return categories.get(c, 'other')

# cat_key('a'), cat_key('A'), cat_key(':'), cat_key(' ') # ('lower', 'upper', 'other', None)


#####################################
#--------------Views----------------#
#####################################

'''
Three ways to view data in dictionary

keys only -> dictionary_name.keys()
values only -> dictionary_name.values()
key/value pairs -> dictionary_name.items()

These views produce iterable objects, positional order is maintained across views

Views are read only, can't update dictionary using views
Keys views behave like sets (unique, hashable) -> can do set operations using keys
We can do the same for items if all values are hashable

'''
# Example 4a. .keys()

bball = {'team': 'Boston Redsox', 'wins': {'2018': 108, '2017': 93}}
bball.keys() # dict_keys(['team', 'wins'])

# Example 4a. .values()

bbal.values() # dict_values(['Boston Redsox', {'2018': 108, '2017': 93}])

# Example 4c. .items()

bbal.items() #dict_items([('team', 'Boston Redsox'), ('wins', {'2018': 108, '2017': 93})])

#####################################
#------------Iteration--------------#
#####################################

# Example 5a. single dictionary

person = {'name': 'John', 'age': 26}

for key in person.keys():
    print(person[key])

for value in person.values():
    print(value)

for key, value in person.items():
    print('{}: {}'.format(key, value))

# Example 5b. dictionary of dictionaries

trees = {
    "tree1": {"name": "Sycamore", "age": 47, "leaf_structure": "palmate"},
    "tree2": {"name": "Maple", "age": 18, "leaf_structure": "palmate"}
}

# indexing
tree['tree1']['name']
treetree['tree1']['name']['leaf_structure']

# looping
for key in trees.keys():
    print(f"{key}")
    #print(trees[key])

for value in trees.values():
    print(f"{value}")

for key, value in trees.items():
    print(f"{key}: {value}")

# Example 5c. list of dictionaries

trees = [
    {"name": "Sycamore", "age": 47, "leaf_structure": "palmate"},
    {"name": "Maple", "age": 18, "leaf_structure": "palmate"}
]

for tree in trees:
    print("Tree keys:")
    for key, value in tree.items():
        print(f"{key}, {value}")
# compare

for t in trees:
    print(f"{t['name']} is {t['age']} years old")

# 5d. Nested dictionaries - use case create a grid of x, y coordinates and find distance of each point from origin

x_coords = (-4, 7, 0, 2, 5)
y_coords = (4, 1, 0, 8, 9)

# generate all combinations of x,y tuples

grid = []

for x in x_coords:
    for y in y_coords:
        grid.append((x, y))

# grid = [(x,y) for x in x_coords for y in y_coords] # using dictionary comprehension

# calculate distancea for points from origin

import math # will use .hypot() method

math.hypot(1, 1) # distance from origin (0, 0) is sqrt of 2

grid_extent = [(x,y, math.hypot(x,y)) for x, y in grid)] # gives x, y and distances from origin

# we want dict where we can look up coord pair and get distance value

grid = {(x,y): math.hypot(x,y) for x in x_coords for y in y_coords}

grid[(5,8)] # example for how to look up distance from the coordinates

comp_dict = {x:x**2 for x in range(20) if x%2 ==0}


#########################################
#--------------Operations---------------#
#########################################


# Example 6a. Membership testing

data = dict(a=1, b=2, c=3)

'a' in data # looking for keys in hash table

# Example 6b - merge two dicts

data1 = dict(zip('abcdu', (1,2,3,4,5)))
data2 = dict(zip('tuvwx', (6,7,8,9,10)))

data1 | data2 # merge -> new dict, |= Inplace merge


# Example 6c. Key operations

data1.keys() & data2.keys() # common keys
data1.keys() - data2.keys() # difference: keys in data1 not in data2
data1.keys() ^ data2.keys() # keys unique to each



#############################################
#--------------Comprehension----------------#
#############################################

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

dict1_cond = {k:v for k,v in dict1.items() if v>2}

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)

dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

dict2_tripleCond = {k:v for (k,v) in dict2.items() if v>2 if v%2 == 0 if v%3 == 0}
print(dict2_tripleCond)

dict2_bools = {k:('even' if v%2==0 else 'odd') for (k,v) in dict2.items()}
print(dict2_bools)

nested_dict = {'first':{'a':1}, 'second':{'b':2}}

float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}

print(float_dict)


###########################################
#----- Collecting JSON Data: APIs --------#
###########################################

'''
JSON - Javascript Object Notation
    text-based object serialization
    common for web APIs and data interchange
    supports limited data types:
        strings -> uses "" not '', unicode
        numbers -> all floats no distinction
        booleans -> true, false
        arrays(lists) -> [] delimited by square brackets, ordered
        dictionaries -> {"a":1, "b", "python} keys must be string, values can be any supported data type, unorder keys
        empty value -> null


JSON often used for serializing and deserializing Python dictionaries

import json        load (JSON file -> Python), loads (JSON string -> Python)
write to json        dump (Python -> JSON file), dumps (Python -> JSON string)

JSON OBJECT -->

person = {
    "name": "Alice",
    "age": 30,
    "city": "Denver"
}

JSON STRING -> can't index by key

person_json = '{"name": "Thomas", "age": 30, "city": "Denver"}'

JSON keys need to be strings <--> Python keys just need to be hashable
JSON value types are limited <--> Python dictionary values can be any data type
'''

import json

import requests # you will learn this in COMP3006


### Example 1. Collect JSON Data From Internet. Make a GET request to the API


def get_data(url):

    response = requests.get(url) # returns a response object
    if response.status_code != 200:
        raise Exception(f'API response: {response.status_code}')

    else:
        response = response.json() # returns a list or dictionary based on the data source
        return response


raw_data = get_data('https://data.ny.gov/resource/3x8r-34rs.json')

raw_data[0]
len(raw_data)

first_keys = (raw_data[0].keys())

print(first_keys)

### Example 5. Select all keys in the entire dataset

features = sorted([key for dictionary in raw_data for key in dictionary])

print(features)


features = sorted({key for dictionary in raw_data for key in dictionary})

print(features)

#################################
#----- Accessing Data ----------#
#################################

### Example 6. Select value for a given key in the first dictionary

proj_num = raw_data[0]['project_number']
print(proj_num)

### Example 7. Looping to collect all values for a given key


counties = set()
for dict_ in raw_data: # taking dicts from the list
    try:
     c = dict_['county'] # accessing keys
     #c = dict_.get('county') # returns None if key is not found
     counties.add(c)
    except KeyError:
        print('Missing key: county')
        continue
print(f'\n\nThere {len(counties)} in this data set.\n\nThey are: {counties}')

### Example 8. Set Comprehension

counties = {dict_["county"] for dict_ in raw_data if "county" in dict_}
print(counties)

### Example 9. Subset the data: note duplicate entries

data_subset = [{key: dict_[key] for key in ("county", "city")} for dict_ in raw_data if "county" in dict_ and "city" in dict_] # what happens if you try using a dict comprehension

print(len(data_subset))

print(data_subset)

# Collect unique entries - using get() method

data_subset = {(d.get('county'), d.get('city')) for d in raw_data}

print(len(data_subset))

print(data_subset)


##### Access JSON via. API --> Write selected data to CSV file with csv module #####

# Prepare data for CSV
import csv


my_energy_data = requests.get('https://data.ny.gov/resource/3x8r-34rs.json')

ny_energy= my_energy_data.json()

csv_data = [] # this will be a list of lists

for item in ny_energy:
    if 'project_number' in item and 'city' in item and 'program_type' in item:
        csv_data.append([item['project_number'], item['city'], item['program_type']])

print(csv_data) # always evaluate results at each step before proceeding to the next

## Write to CSV file with standard python methods -basically creating multi-line, comma delimited, txt entries

csv_data = "Project Number,City,Program Type\n"  # CSV headers

for item in ny_energy:
    if 'project_number' in item and 'city' in item and 'program_type' in item:
        csv_data += f"{item['project_number']},{item['city']},{item['program_type']}\n"

print(csv_data[:1000])

### Write data to CSV file

with open('output.csv', 'w') as f:
    f.write(csv_data)
