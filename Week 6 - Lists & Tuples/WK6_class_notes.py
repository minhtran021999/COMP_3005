

#####################
#------Lists--------#
#####################

'''

Key Characteristics of lists

1. ordered - allows indexing
2. Mutable
3. Heterogenous
4. Permit duplicates
5. Defined by square brackets []



List Dot methods

append - append object to end of list
clear - remove all items from list
copy - returns shallow copy of list
count - return number of occurrences of value
extend -  extend lis by appending elements from an iterable
index - return first index of a value
insert - insert object before index
pop - remove and return item at index
remove - remove first occurrence of value
reverse - reverse list in place
sort - sort list in ascending order (in place) and return None. Include reverse = True to sort descending

print(help.list.method) # use this format for more information

To see all of the dot methods:

print([method for method in dir(list) if not method.startswith('__')])
'''

# Example 1. Review: list creation

new_list = [] # takes no arguments but can contain any number of elements to define initial content

new_list = list() # accepts 0 (empty list) or 1 argument (single iterable object)

new_list = [34, '67', [3,4,5]]

# new_list = list(34, '67', [3,4,5]) 

# Try iterating over mew_list using [34, '67', [3,4,5]] vs list(34, '67', [3,4,5]) 

for i in new_list:
    print(i)

# Iterable - a python object that can be looped over one item at a time

'''

LIST SLICING

Basic Syntax: list[start:stop:step]

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Index:    0    1    2    3    4    5    6    7
# Neg Index:-8   -7   -6   -5   -4   -3   -2   -1

Start & Stop

my_list[2:5]	['c', 'd', 'e']	Elements from index 2 (inclusive) up to index 5 (exclusive).
my_list[:4]	['a', 'b', 'c', 'd']	Elements from the beginning (default start=0) up to index 4 (exclusive).
my_list[5:]	['f', 'g', 'h']	Elements from index 5 (inclusive) to the end (default stop=len(list)).
my_list[:]	['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

Negative Indices

my_list[-3:]	['f', 'g', 'h']	The last three elements (from index -3 to the end).
my_list[:-2]	['a', 'b', 'c', 'd', 'e', 'f']	Elements from the beginning up to the second to last element (exclusive).
my_list[1:-1]	['b', 'c', 'd', 'e', 'f', 'g']

Step Value

my_list[::2]	['a', 'c', 'e', 'g']	Every second element starting from the beginning.
my_list[1::2]	['b', 'd', 'f', 'h']	Every second element starting from index 1 (the second element).
my_list[::3]	['a', 'd', 'g']	Every third element.

List Reversal

my_list[::-1]	['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']	Reverses the list by stepping backward by 1.
my_list[7:0:-2]	['h', 'f', 'd', 'b']	Steps backward by 2, starting at index 7 and stopping before index 0.

'''

# Example 2. Write an expression that prints the value 6 from the list:

lst =[3.0, 'tom', [2, (5, 6, 4)]]
print(lst[2][1][1])



lst =  ['a', 'b', 'c', 'd', 'e', 'f']

# Now print ['a', 'c', 'e'], ['b', 'd', 'f'], ['f', 'd', 'b']

print(lst[::2]) 
print(lst[1:6:2])  
print(lst[::-2]) 


'''
The slice [::-2] is a form of Python's slice notation. Here's what it means:

The first colon : means "start at the beginning of the list"
The second colon : means "go until the end of the list"
The -2 means "step through the list in steps of -2"
So, [::-2] means "create a new list that starts from the end of the original list and steps backwards in steps of 2".
'''


###############################
#------Iterating Over Lists---#
###############################

# -------------------Basic ----------------------------

# Compare results for the following 3 loops

# Example 3. home_list = [1,'tom', 4.56, 5, 'ellen', 7]

for i in home_list:
    print(i)
    
for i in range(homelist): 
   print(i)

for i in range(len(home_list)):
    print(f'index = {i}, value = {home_list[i]}')

for index, value in enumerate(home_list):
    print(f'index = {index}, value = {value}') 

# -------------------Nested Lists ----------------------------
    
# Open your browser to pythontutor.com, click on 'edit code and get ai help' and paste the following code into the editor. Click 'Visualize Execution' and step through the code to see how Python iterates through the nested lists.

# Example 4

short_list = [[1,2,3], [4,5], 'hello']
for var in short_list:
    for element in var:
        print(element) # treats string as a container

short_list = [[1,2,3], [4,5], 3, 'hello'] # TypeError: 'int' object is not iterable

# -------------------Nested with Except----------------------------

# Example 5. The following will throw an error because we our inner loop (val in sublst) is trying to iterate over a single int value (5), which is not a sequence. We can catch this error with a try/except block.

new_homelist = [[], 'hello', 5, [4.0, 4.3, 7.6]]

for sublst in new_homelist:
    try:
        for val in sublst:
            print(val)
    except TypeError:
        print('Type error occurred: sublist may not be iterable')

# Example 6. A nested loop that includes enumerate

for index, value in enumerate(new_homelist):
    print(f'index in new_homelist = {index}, value in new_homelist = {value}')
    try:
        for val in value:
            print(val)
    except TypeError:
        print('Type error occurred: sublist may not be iterable')
        

#######################################
#------Mutability and Aliasing--------#
#######################################

'''
In Python, an object is considered mutable if it can be changed after it is created, and immutable if it cannot be changed after creation.

For example, lists, dictionaries, and sets are mutable. This means you can add, remove, or change elements in a list or dictionary after it is created:

On the other hand, strings and tuples are immutable. Once a string or tuple is created, you cannot change its content:

primitives such as ints, floats, booleans, and strings are also immutable (prove this) with id()
'''

# Example 7. Data primitives (eg. int, str) are immutable: what would be a good test of this?

ten = 10
print(id(ten)) #140707363382344

ten = 11
print(id(ten)) #different memory location

# Example 8. Lists are mutable:

lst = [1,2,3]
print(lst)
print(f'{id(lst)}\n\n')

lst.append(4)
print(lst)
print(id(lst)) # same memory location

# Example 9. Aliasing - take care when working with mutable objects

lst2 = lst
print(id(lst2)) # same memory location as lst

lst2 == lst
lst2 is lst

lst2.append(22) # modify lst2

print(lst) # aliasing can cause unwanted side effects

# Are these aliases?

test1 = [1,2,3]
test2 = [1,2,3]

print(id(test1), id(test2)) # different memory locations

# we can also compare memory locations with the is keyword

test1 is test2

#############################################
#------Membership & Basic Operations--------#
#############################################
 
# Example 10. Membership: 'in', 'not in'

fruit = ['apple', 'banana', 'orange', 'grape']
'grape' in fruit # True
'strawberry' not in fruit # True

# Example 11. Operations: len(), max(), min(), sum()

animals = ['dog', 'cat', 'bird', 'fish']
print(len(animals)) # 4
print(max(animals)) # fish #strings are compared letter by letter using the ASCII value of the lexical order based on unicode code point value, lower case have higher points than upper
print(sum(animals)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Example 12. Concatenation: +, Repetition: *

fish = ['shark', 'tuna', 'salmon', 'trout']
animals = ['dog', 'cat', 'bird', 'fish']
print(animals + fish)
print(animals * 4)
print(fish * animals) # TypeError: can't multiply sequence by non-int of type 'list'



#################################
#------  class exercise --------#
#################################

'''
read in the csv class_csv.csv

separate each column into a separate list, skip observations that != 4 columns, as well as values which cant be converted to ints. 

'''



filename = './class_csv.csv' # . singl this directory
dataset = []
try:
    with open(filename, 'r', encoding = 'UTF-8') as file:
        for row in file:
            row_data = row.strip().split(',') # -> split() creates a list of substrings
            dataset.append(row_data)
            
except FileNotFoundError as e:
    print(f'There was an error with file read in: {e}.')
#



req_cols = 4 

head_count = []
start_year = []
salary = []
annual_sales = []

for line in dataset[1:]:

    # Check Length (Too Short/Too Long)
    if len(line) != req_cols:
        if len(line) < req_cols:
            print(f'Skipping row {line} due to missing columns (found {len(line)}, expected {req_cols}).')
        else: 
            print(f'Skipping row {line} due to too many columns (found {len(line)}, expected {req_cols}).')
        continue 
        
    temp_line = []
    try:
        for item in line:
            int_item = int(item) 
            temp_line.append(int_item)
    except ValueError:
        print(f'There is a value error, skipping observation {line} due to non-integer or empty value.')
        continue 
    
    head_count.append(temp_line[0]) 
    start_year.append(temp_line[1])
    salary.append(temp_line[2])
    annual_sales.append(temp_line[3])


print(f'Head Count Data: {head_count}')
print(f'Annual Sales Data: {annual_sales}')




#########################
#------  Tuples --------#
#########################

'''
Key Characteristics:

1. Immutable
2. Ordered - can be indexed
3. Allow duplicates
4. Heterogenous

Tuples differ from lists in that they are immutable - cant add, remove, or modify elements in place

Tuples are sometimes more computationally efficient than lists because they are immutable - allows for greater storage and retrieval efficiency. Useful for static collections.

Tuples can be indexed and sliced. Indexing starts at 0 and negative indexing starts at -1. Slicing is done with a colon and can be used to access a range of values.


Tuple Dot Methods:

1. count() - returns the number of occurrences of a value
2. index() - returns the first index of a value

'''

#######################################
#----------Creating Tuples------------#
#######################################

# Example 13 - syntax options

tup = (1,2,3)

tup = 1, 2, 3 # parentheses are optional

tup_maybe = (1)
print(type(tup_maybe)) # this is actually a type int

tup = (1,) # single element tuple, try without the comma
print(type(tup))

tup = () # this is a tuple

##############################################
#----------Assignment & Unpacking------------#
##############################################

# Example 14. Unpacking

x, y = (5, 'jennifer')
print(y)

# swapping values

x = 12
y = 13

y, x = x, y
print(x,y)

# unpacking a tuple

tuple_example = (1, 2, 3, 4, 5)
v, w, x, y, z = tuple_example
print(v, w, y)

for index, value in enumerate(tuple_example):
    print(index, value)
    
# Example 15. Implicit unpacking using *

# unpacking with * operator during function calls

def add(*args): # recall that this * is used to create a wildcard -> any number of positional args can be passed in.
    return sum(args)

tuple_example = (1, 2, 3, 4, 5)
print(add(*tuple_example)) # try without the * operator -> here we are using * as syntax to unpack a tuple. This is a different application than the wildcard used in our function definition,

'''
When you call add(tuple_example), the add function sees tuple_example as a single argument, so args becomes a tuple of one element, where the single element is tuple_example.
'''

#######################################
#------Mutability and Aliasing--------#
#######################################

'''
In Python, an object is considered mutable if it can be changed after it is created, and immutable if it cannot be changed after creation.

For example, lists, dictionaries, and sets are mutable. This means you can add, remove, or change elements in a list or dictionary after it is created:

On the other hand, strings and tuples are immutable. Once a string or tuple is created, you cannot change its content:

primitives such as ints, floats, booleans, and strings are also immutable (prove this) with id()
'''

# Example 16. Compare list and tuple mutability

lst = [1, 2, 3]
lst[0] = 'hello'
print(lst)


tup = (1, 2, 3)
tup[0] = 'hello' # TypeError: 'tuple' object does not support item assignment

# Example 17. Check memory locations for tuples and aliasing

tup_ten = (10, 10)
print(id(tup_ten)) 

tup_ten = (11, 11)
#print(id(tup_ten)) # different memory location

alias_tup = tup_ten
alias_tup is tup_ten
#print(id(alias_tup)) # same memory location as tup_ten

##### updating a tuple

# Existing tuple
existing_tuple = (1, 2, 3)
print(id(existing_tuple))

# New variable to add
new_variable = 4

# Create a new tuple by concatenating the existing tuple and the new variable
new_tuple = existing_tuple + (new_variable,)

print(new_tuple)  # Output: (1, 2, 3, 4)
print(id(new_tuple))

##############################
#------ Tuple Methods--------#
##############################

# Example 18. tuple built-in methods

[i for i in dir(tup_ten) if not i.startswith('__')]

tupper = (8, 7, 5, 7, 'string')
tupper.count(7) # counts the number of times 7 appears in the tuple
tupper.index(7) # returns the index of the first occurrence of the value


#############################################
#------Membership & Basic Operations--------#
#############################################
 
# Example 20. Membership: 'in', 'not in'

fruit = ('apple', 'banana', 'orange', 'grape')
'grape' in fruit # True
'strawberry' not in fruit # True

# Example 21. Operations: len(), max(), min(), sum()

animals = ('dog', 'cat', 'bird', 'fish')
print(len(animals)) # 4
print(max(animals)) # fish #strings are compared letter by letter using the ASCII value of the letters.
print(sum(animals)) # This produces a Type error, addition not supported

# Example 22. Concatenation: +, Repetition: *

fish = ('shark', 'tuna', 'salmon', 'trout')
animals = ('dog', 'cat', 'bird', 'fish')
print(animals + fish)
print(animals * 4)
print(fish * animals) # TypeError: can't multiply sequence by non-int of type 'tuple'


################################
#------Iterating Over Tuples---#
################################

# -------------------Basic ----------------------------

# Example 23 - different for loop configurations

home_tuple = (1,'tom', 4.56, 5,'ellen', 7)

for i in home_tuple:
    print(i)

for i in range(len(home_tuple)):
    print(f'index = {i}, value = {home_tuple[i]}')

for index, value in enumerate(home_tuple):
    print(f'index = {index}, value = {value}') 

# -------------------Nested ----------------------------

# Example 24 basic nested loop with tuples

short_tuple = ((1,2,3), (4,5), 'hello')
for var in short_tuple:
    for element in var:
        print(element)

short_tuple = ((1,2,3), (4,5), 3, 'hello') # TypeError: 'int' object is not iterable

# -------------------Nested with Except----------------------------

# Example 25. nested loop with exception handling 

new_home_tuple = ((), 'hello', 5, (4.0, 4.3, 7.6))

for sublst in new_home_tuple:
    try:
        for val in sublst:
            print(val)
    except TypeError:
        print('Type error occurred: subtuple may not be iterable')

for index, value in enumerate(new_home_tuple):
    print(f'index in new_home_tuple = {index}, value in new_home_tuple = {value}')
    try:
        for val in value:
            print(val)
    except TypeError:
        print('Type error occurred: subtuple may not be iterable')


##############################
#------ Named Tuples --------#
##############################

'''

Named Tuples will be covered in 3006. I am including it here for those who want to experiment with it.

Named tuples are part of Python's collections module. They are a way to create a tuple with 
named attribute fields (i.e., quick way to create a object/class type). In essence,
they are a class-like structure (sub-class of tuple) used for creating lightweight, immutable objects with field names. 

Named tuples can be used in places where you are handling a set of values and you can use 
names instead of integer indices to access the values. This makes your code more readable 
and self-explanatory.

'''

# Example 19. named tuples

from collections import namedtuple

# Define a named tuple type with the name 'Person' and the fields 'name' and 'age'
Dog = namedtuple('Dog', ['name', 'breed', 'age']) # define a new type (similar to class) named Dog

# Create an instance of a dog type
doggy = Dog(name = 'fido', breed = 'miniature poodle', age = 116)

# Access the fields using dot notation

print(doggy.name)  
print(doggy.age)  

print(doggy)

