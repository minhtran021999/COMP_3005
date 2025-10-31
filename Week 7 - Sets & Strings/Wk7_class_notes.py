

##################################
#------ Sets and Strings --------#
##################################

# Review Challenge: we did this exercise at the start of class.

# Exercise 1 : Loop over the following lists and for each client_name create a text file with
# the 'name of the person_results' and write the corresponding result to the file in a local directory.

client_names = ["Smith", "Roberts", "Ali", "Turnier", "Newman", "Parada"]
results =        [1,          2,      34,       5,         6,       7]

# Here is a solution that takes advantage of the .pop() method

for client in (client_names):
        with open(f"{client}_results.txt", 'w') as write_file:
            write_file.write(str(results[0]))
            results.pop(0)

# Here is a solution that uses the enumerate() method

for ind, client in enumerate(client_names):
    with open(f"{client}_results.txt", 'w') as write_file:
        write_file.write(str(results[ind]))

# Here is a solution based on indices

for i in range(len(client_names)):
    with open(f"{client_names[i]}_results.txt", 'w') as write_file:
        write_file.write(str(results[i]))

# Here is a solution based on the zip() method and indices

for i in zip(client_names, results):
    with open(f"{i[0]}_results.txt", 'w') as write_file:
        write_file.write(str(i[1]))

# The examples listed above are worth studying. Can you explain to somewhat exactly what is happening line by line?

 # sorting function:

for i in range(n - 1):
    for j in range(n - 1 - i):


  #################################
 #---------- HW 7 ---------------#
 #################################

 #Q1 - remove all whitespace and non-alphabetic chars; normalize text to lowercase

 #Q2 - example of a bubble sort (see session slides)

 #n = len('items in list'')

 # loop over list, one pass required for placing last element. Equivalent to 0 to n-2 inclusive. for sorting of this kind, the largest element is pushed to the end
 #for num in range(n-1):
     # compare pairs up to last unsorted element
    #for index in range(n-1-num):

#Q3 - adjacent letter swap.

#for i in range(len(string) - 1) #  we swap i and i+1 -> we dont want to go beyond string


 #################################
#---------- Sets ---------------#
#################################

'''
Important concepts:

Hashability - a Python object is considered hashable if it is immutable. It's identity can be stored as a integer value for the
pruposes of efficient look-up & retrieval (using hash tables). A immutable object is not always hashable -> if it contains
mutable elements. For example, a tuple that contains a list.

Sets:

1. Sets elements are unique, duplicates not allowed
2. Sets are unordered, do not support indexing or slicing
3. Sets are mutable (not hashable), elements can be added or removed, but the elements themselves are immutable
4. Sets can only include immutable elements
5. Sets are iterable

Frozensets: immutable (hashable), iterable, sets. Common uses include as keys in dictionaries, and elements of other sets.

Importance:

1. sets only store unique elements, good for removing duplicates
2. sets support mathematical operations: union, intersection, symmetric difference, etc. Good for finding common elements between datasets,
    or unique elements, or eliminate values in one dataset based on presence in another.
3. sets allow for membership testing - good for data validation, filtering, searching.
4. unique counts
5. frozensets allow lookup using hash tables -- useful for searching. This is not the case for sets.
'''

##########################################
#---------- creating Sets ---------------#
##########################################


# 1. Using curly braces
s = {1, 2, 3}

{i for i in range(1, 7)} # we can build longer sets with set comprehension

# 2. Using the set() constructor

s = set([1, 2, 3])

type(s)

'''
The example above is a bit tricky. Sets can't include elements that are mutable and a list is mutable. What we are actually creating here is a set from a list. It's analogous to casting a data type.
'''

s = set(1,2,3,4) # TypeError: set expected at most 1 argument, similar to list() the set() form only allows one parameter

#3. Empty set restrictions

s = set()
print(type(s)) # <class 'set'>

s = {}  # This is a dictionary, not a set, it won't work
print(type(s)) # <class 'dict'>

#4. Sets and iterables

s = set('hello_again') # try printing this!
s = set([1, 2, 3])

'''The reason set('hello_again') results in a set of separate characters instead of a single string is because the set() function in Python iterates over the given iterable (in this case, the string 'hello_again') and adds each element to the set.'''

#4. Frozensets
fs = frozenset([1, 2, 3]) # we are converting a list to a frozenset
type(frozenset)



##########################################
#----------   hashability ---------------#
##########################################

'''frozensets are hashable, which means they can be used as keys in dictionaries or as elements in other sets. They can also be used as keys for caching mechanisms and for mutliple-thread use without data corruption'''

# TypeError: unhashable type: 'set'

s = {1, 2, 3}
print(hash(s))  # TypeError: unhashable type: 'set'; mutable objects don't have hash values

fs = frozenset([1, 2, 3]) # frozensets are immutable & hashable
print(hash(fs))

print(hash('COMP4401')) # hashable. The has function is operating on the string, this is not a set

# Mutable and Immutable variables within a  - all elements in sets must be immutable

s = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'. Note diff in behavior: set = {[3,4]}
s = {1, 2, (3, 4)} # recall that tuples are immutable
s = {1, 2, 'thomas'}
s = {1, 2, {3, 4}}  # TypeError: unhashable type: 'set'
s = set((1,2,3,4))

##########################################
#--------- Properties: Review  ----------#
##########################################

# 1. Sets and frozensets are unordered --> elements are not indexed

s = {1,2,3,4,5,6,76}
print(s[4]) # TypeError: 'set' object is not subscriptable. An object is "subscriptable", it means that it can use the subscript notation (square brackets []) to access or set values.

fs = frozenset([1, 2, 3])
print(fs[0][1]) # TypeError: 'frozenset' object is not subscriptable

print(list(fs)[1]) # We can access elements of a set by converting to a data type that is subscriptable

# 2. Sets and frozensets are iterable

s = {1,2,3,4,5,6,76}
for var in s:
    print(var)

text = 'I will be going to the store to get some milk today'
txt = set(text.split(' ')) # print this, try without split first

sorted_txt = sorted(txt) # reverse argument: reverse = True, produces a sorted list
print(sorted_txt)

for word in sorted(txt): # iterating over a set
    print(word, end = ' ')

'''Note:
    list.sort() is an in-place sorting method for lists; modifies the list directly
    sorted() is a built-in function that returns a new sorted list from any iterable (list, tuple, string, set, etc.).
        It does not modify the original data.

    sorted() converts the set into a list and then uses lexicographical order (based on Unicode point for each char) to sort a string or set of words
'''

# 3. Sets are mutable, frozensets are immutable

s = {1,2,3,4,5,6,76}
s.add(7)
print(s)

fs = frozenset({1,2,3,4,5,6})
fs.add(7)
print(fs) # results in attribute error

# 4. Sets and frozensets can only include immutable elements

s = {1,2,3,4,5,6,76}
s.add([7,8]) # TypeError: unhashable type: 'list'
s.add((7,8))
print(s)

# 5. Sets and frozensets can only include unique elements

s = {1, 2, 3, 4, 5, 5, 6, 76}
s.add(7)
s.add(7)
print(s)

##########################################
#---------- Set Membership  -------------#
##########################################

fruits = {'apple', 'banana', 'cherry'}
ape = 'chimpanzee'

if ape in fruits:
    print(f'{ape} is in the set')
else:
    print(f'{ape} is not in the set')

##########################################
#-------------   Methods  ---------------#
##########################################

set_methods = [x for x in dir(set) if not x.startswith('_')]
print(set_methods)

# it's a good idea to commit the syntax of comprehension to memory. This is an example of list comprehension. Below is an example of set comprehension.

set_methods = {x for x in dir(set) if not x.startswith('_')}


#######################################
#---------- Set Methods  -------------#
#######################################

#. Add -- adds an element to the set
#2. Remove -- will raise an error if the element is not in the set, compare to discard
#3. Discard -- will not raise an error if the element is not in the set
#4. Pop -- removes a random element from the set
#5. Clear -- removes all elements from the set
#6. Union (|) -- returns a new set with all items from both sets
#7. Update (x1 |= x2) -- inserts the items in set2 into set1
#8. Intersection (&) -- returns a new set with items that are in both sets
#9. Intersection_update (&=) -- removes the items that are not present in both sets
#10. Difference (-) -- returns a set that contains the items that only exist in set1, and not in set2
#11. Difference_update (-=) -- removes the items that exist in both sets
#12. Symmetric_difference (^) -- returns a set that contains all items from both sets, except items that are present in both sets
#13. Symmetric_difference_update (^=) -- inserts the symmetric differences from this set and another
#14. isdisjoint -- returns True if no items in set1 are present in set2
#15. issubset (<=, < proper) -- returns True if all items in the set exists in the specified set
#16. issuperset (>=) -- returns True if all items in the specified set exists in the original set
#17. copy -- returns a copy of the set
#18. difference -- returns a set containing the difference between two or more sets
#19. symmetric_difference -- returns a set with the symmetric differences of two sets

#NOTE: Since frozensets are immutable, they do not accept the methods that modify sets in-place such as add, pop, or remove


##########################################
#---------- Set Operations  -------------#
##########################################

s = {'apple', 'banana', 'cherry'}
s.add('orange')
s.add('apple')
s.add([2,3,4]) # TypeError: unhashable type: 'list'
s.remove('banana')
s.discard('chocolate bars')
print(s)


s1 = {3, 4, 5, 7, 8, 9, 10, 23}
s2 = {5, 3, 7, 8, 2, 22, 45}

print(s1.union(s2)) # -> |
print(s1.intersection(s2)) # -> &
print(s1.difference(s2)) # -> -
print(s2.difference(s1))
print(s1.symmetric_difference(s2)) # -> ^
print(s1.isdisjoint(s2))

s1.intersection_update(s2)
print(s1)

######################################################
#---------- Subsets (Proper & Improper) -------------#
######################################################

A = {1, 2, 3, 4}
B = {1, 2, 3}
C = {1, 2, 3, 4}

print(B.issubset(A))  # Outputs: True, B is a subset of A
print(A.issuperset(B))  # Outputs: True, A is a superset of B
print(C.issubset(A))  # Outputs: True, C is also an improper subset of A

# To check if B is a proper subset of A, we can check if B is a subset of A and B is not equal to A
print(B.issubset(A) and B != A)  # Outputs: True, B is a proper subset of A

set(' abc def ghi jkl mno'). issuperset('hi mom')

#########################################
#---------- tiny challenge -------------#
#########################################

# use mathematical set operations to combine sets
{10, 20, 30} and {5,10, 15, 20} # and produce the following. Do this with set methods and set operations (e.g., union, |)

s1 = {10, 20, 30}
s2 = {5,10, 15, 20}

{30}
{5, 15, 30}
{5, 10, 15, 20, 30}
{10, 20}


# Answers
s1.difference(s2) #s1 - s2
s2.symmetric_difference(s1) #s1 ^ s2
s1.union(s2) # s1 | s2
s1.intersection(s2) #s1 & s2


##################################
#---------- Strings -------------#
##################################

'''
Concepts:

Strings are a sequence of characters. They are immutable, meaning they cannot be changed after they are created.They are also iterable and ordered.

Raw strings are useful when you want to include backslashes in your string and don't want them to be interpreted as escape characters.

The string class includes a wide variety of dot methods. You will need to experiment with these methods to become familiar with them. The time you invest will be well worth it -- particularly for data cleaning and text analysis.

'''

##################################
#---------- Methods -------------#
##################################

str_methods = [x for x in dir(str) if not x.startswith('_')]

print(str_methods)

# Applying string methods - what is the differnce between isalpha, isdecimal, isdigit, isnumeric, and isascii?

'''
isalpha(): This method returns True if all characters in the string are alphabetic (letters), and False otherwise. It doesn't consider numeric characters, punctuation, or whitespace as alphabetic. For example:

isdecimal(): This method returns True if all characters in the string are decimal characters (0-9), and False otherwise. It doesn't consider non-decimal characters or other numeric characters like fractions or exponents as

isdigit(): This method returns True if all characters in the string are digits (0-9), and False otherwise. Unlike isdecimal(), it also considers certain other representations of numbers, like superscripts and subscripts, as digits.

isnumeric(): This method returns True if all characters in the string are numeric characters, including digits, decimal points, superscripts, subscripts, and other numeric representations used in various languages and scripts. It's a more inclusive method than isdigit() and isdecimal()

isascii(): This method returns True if all characters in the string are ASCII characters (including letters, digits, punctuation, and whitespace), and False otherwise. It doesn't consider non-ASCII characters as valid

'''



string_list = ['zZebra99_44@', 'zZebra99', 'zZebra99_44', 'winny.pooh@du.edu', 'abCdedfG', '0965', '1,000', '54.3', '3/4']

def str_test(string):
    for i in string:
        print(f'\nOur string example is : {i}.\n')
        print(f'isalpha == {i.isalpha()}')
        print(f'isdecimal == {i.isdecimal()}')
        print(f'isdigit == {i.isdigit()}')
        print(f'isnumeric == {i.isnumeric()}')
        print(f'isascii == {i.isascii()}')


str_test(string_list)

# To evaluate strings that represent valid floating point values

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

print(is_float("3.54"))  # True
print(is_float("3.54a"))  # False



############################################
#---------- Splitting Strings -------------#
############################################

'''
\r or 0xD -> carriage return. moves cursor to the beginning of the line
\f or 0xc -> form feed. moves carriage to beginnin of the next page
'''

#########################################
#---------- tiny challenge -------------#
#########################################

# Create a list with sublist of sentences, remove all \r and '.' and empty strings and/or white spaces at the beginning and end of a sentence.


string= 'This is the first string. \r This is my second string.'

sentences = []
for s in string.split('.'):
    s = s.replace('\r', '').strip('.') # removes leading or trailing '.'
    print(s)
    if s: # try removing just this line (& correct indentation on the following) and see what happens when you print, can you explain the difference?
        sentences.append([s.strip()])
print(sentences)

'''
string.split('.') = ['This is the first string', '\r This is my second string', '']

note: split()->When set to None (the default value), will split on any leading or trailing whitespace
        character (including \n \r \t \f and spaces) and will discard
        empty strings from the result


'''

# Another example of list comprehension: try to understand the syntax and the order of the expressions

[[x.strip()] for x in (sentence.replace('\r', '').strip('.') for sentence in string.split('.')) if x.strip()]

# Partitioning a string

string= 'This is the first string.\r This is my second string.'
print(string.partition('This'))
print(string.rpartition('This'))

'''
The partition() method splits the string into three parts:

The part before the specified separator (substring)
The separator substring itself
The part after the separator substring

Since the string starts with 'This', the part before the separator is an empty string ''.
'''

# Using .replace() to modify a string

str = 'This is a string test'

str.replace('test', 'bean')

# to get rid of all whitespace
#
str.replace(' ', '')

############################################
#---------- Sorting Strings -------------#
############################################

# Example 1. Sort the characters in a string

string_dog = "    Lupine is my dog's Name"
sorted(string_dog) # based on unicode values - > upper case letters come before lower case letters, digits before letters

# Example 2. Sort the words in a string

string_dog = "    Lupine is my dog's Name"
sort_dog = sorted(string_dog.split(' '))

# Using list comprehension

[w for w in sort_dog if w != '']


######################################
#---------- Raw Strings -------------#
######################################

# raw strings -> treat escape characters '\' as literals

s = 'lang\tver\nPython\t3'
print(s)
[i for i in s]

s = r'lang\tver\nPython\t3'
print(s)
[i for i in s] # note the difference


# Time permitting code reading exercise

### Class review: reading code and try to guess what unfamiliar methods are doing.


import os
from pathlib import Path

directory_path = os.getcwd()

def concat_csv_to_csv(directory_path):
    combined_data = []
    first_file_columns = None
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.csv'):
            try:
                file_path = Path(directory_path) / file_name
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = file.readlines()
                if first_file_columns is None:
                    first_file_columns = data[0].strip().split(',')
                else:
                    combined_data.extend(data[1:])
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

    with open(Path(directory_path) / 'combined_data.csv', 'w', newline='', encoding='utf-8') as outfile:
        outfile.write(','.join(first_file_columns) + '\n')
        for line in combined_data:
            outfile.write(line)


concat_csv_to_csv(directory_path)
