

#### Class 3. CONDITIONAL PROGRAMMING AND CONTROL FLOW ####

''''
Homework 2 video to be posted
Go over quiz questions - Asynch
Go over very basics of a list
Go over Week 3 homework


If Else Elif Statements
While Loops
For Loops


IF statements - evaluates an expression and chooses what part of the code to execute

Else - this clause is optional but helps make our work explicit

Elif - employed when there are more than two paths to choose from

Whenever we have conditions expressed as equalities or inequalities (==, !=, <, >, <=, >=), 
the associated numbers represent boundaries

'''

#### REVIEW ####

'''

Short circuit evaluation - Short-circuit evaluation is a technique in which a logical expression is 
evaluated only up to the point where the final outcome is already determined.

x = 1/0

print(x)

print((2 < 3) or 1/0) # (2 <3) evaluates to True. With 'or' so does the entire statement, avoiding XeroDivisionError


Additional conditionals

Identity: is, is not - checks if two variables point to same object in memory
Membership: in, not in - checks for presence of a value in a sequence, tests if element is member of a collection

'''


##### CHALLENGES #####

'''

Problem. Sensor measurement range

Problem: You are monitoring sensor readings in a laboratory instrument. The device should
produce readings within a specific range, but occasionally produces outliers due to interference.
You need to count how many consecutive valid readings occur before encountering an invalid
measurement.

Detailed Instructions:

Prompt user to enter control limits by asking: "Enter lower control limit:" and "Enter upper
control limit:"

Repeatedly ask for sensor measurements: "Enter next measurement (or 'stop' to end):"
Count consecutive measurements that fall within the control limits
Stop counting when either: user enters "stop" OR a measurement falls outside the acceptable
range

Display: "Consecutive valid measurements: [count]"
If stopped due to out-of-range value, also display: "Out-of-range value detected: [value]"


'''

# Soln 1:

def quality_control_counter():
    """
    Monitor consecutive valid sensor readings within acceptable control limits.
    Counts consecutive measurements until an invalid reading or user stops input.
    
    Returns:
        None: Prints count of consecutive valid measurements and stopping reason
    """
    # Get control limits from user
    lower_limit = float(input("Enter lower control limit: "))
    upper_limit = float(input("Enter upper control limit: "))
    
    consecutive_valid_count = 0
    
    print(f"Monitoring readings within range {lower_limit} to {upper_limit}")
    
    # Continue until out-of-range measurement or user stops
    while True:
        measurement_input = input("Enter next measurement (or 'stop' to end): ")
        
        if measurement_input.lower() == "stop":
            print(f"Consecutive valid measurements: {consecutive_valid_count}")
            break
        
        measurement = float(measurement_input)
        
        # Check if measurement is within control limits
        if lower_limit <= measurement <= upper_limit:
            consecutive_valid_count += 1
            print(f"Valid reading #{consecutive_valid_count}: {measurement}")
        else:
            print(f"Consecutive valid measurements: {consecutive_valid_count}")
            print(f"Out-of-range value detected: {measurement}")
            break


# Execute the function
quality_control_counter()



##### CONDITIONAL STATEMENTS: TERNARY OPERATORS #####

# Example 1. Basic If else form

a = 5

if num < 25:  # note syntax
    b = 'a < 25' # indent 4 spaces (1 tab)
else:
    b = 'a > 25'

print(b)


# Ternary Operator - short version of an if/else statement 

b = 'a < 25' if a < 5 else 'a > 5'

print(b)


# The basic syntax for a ternary operator is: "condition ? value_if_true else value_if_false"


#### SWITCH STATEMENTS - If, Elif ##### 

'''
A switch statement is a control flow structure that allows a program to test a value against a 
list of possible cases. 

The program then executes the block of code associated with the first matching case. 
Finally, an optional else statement at the end acts as a default case. 
'''

score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(f"The grade is: {grade}") # Output: The grade is: B



#### NESTED IF ELSE STATEMENTS ##### 

'''
A nested if-else statement is a conditional statement that contains another if-else statement 
within its code block. This structure allows you to test multiple layers of conditions, 
where the inner condition is only evaluated if the outer condition is true.
'''

age = 37
bmi = 17

if age < 45:
	if bmi < 22:
		risk = 'low'
	else:
		risk = 'medium'
else:
	if bmi < 22:
		risk = 'medium'
	else:
		risk = 'high'
print(risk)


# Creating abstraction - consider interpretability

young = age < 45
slim = bmi < 22

if young and slim:
	risk = 'low'
elif young and not slim:
	risk = 'medium'
elif not young and not slim:
	risk = 'medium'
elif not young and not slim:
	risk = 'high'
print(risk)


##### VERY BASIC LISTS ######

'''
A built_in data structure that stores an ordered collection of items in a single variable. 

1. ordered
2. mutable
3. Allow duplicates
4. Heterogenous

'''

# Creating lists - [] and list() both produce lists but behave differently

empty_list = []
empty_list = list() 

print(list('hello'))
print(list(range(10)))
print(list('house', 45, 6.7, ['w','e',3])) # this will throw an error using list()
print(['house', 45, 6.7, ['w','e',3]])

# Accessing a list element(s) via. indexing

eg_list = [5,8,2,4]


print(eg_list[1])
print(eg_lst[-1]) # reverse indexing



##### FOR LOOPS #####

'''
for-loops - A for-loop is a control structure that repeats a block of code a 
predetermined number of times or iterates over a collection of items. 

There are several ways to write basic for-loops

1. Basic iteration over collections
2. Using range() for numeric sequences
3. Using enumerate() for index-value pairs
4. Using zip() for multiple sequences
5. List comprehension
6. Nested for-loops
'''


# 1. Basic iteration over collections - (we will demonstrate with lists and strings)

for item in [4, 5, 7, 8]: # using a list
	print(item)
    
# why might the follow approach result in a TypeError? Hint: investigate the different options for constructing a list. 

for item in ['apple', 7, 5.6, [5,6,7,8]]:
    print(item)
    
# flatten the list

def flatten_list(nested_list)

    flat_list = []

    for item in nested_list:
        if isintance(item, list):
            sub_list = flatten_list(item)
            for sub_item in sub_list:
                flat_list.append(sub_item)
        else: 
            flat_list.append(item)
        return flat_list
        
flatten_list(['apple', 7, 5.6, [5,6,7,8]])


# 2. Range() attributes in a for loop. default starting point is 0 for numbers: inclusive at start point & exclusive at end point. Includes attributes (start, stop, step)


for index in range(10): # loops from 0 - 9
	print(index)

for index in range(1, 10): # loops from 1 -10
	print(index)

for index in range(1,20,3): # loops from 1 to 19 every third element
	print(index)

for index in range(10, 0, -1):
	print(index)
    
for index in range(0, 10, -1): # wont throw an error because iterating over an empty sequence and print is never executed
    print(index)

# 3. Summation in a for loop using an augmented statement

total = 0

for index in range(5):
	total += index # augmented statement
print(total)


# 4. For loop with continue statement and a condition ---> what is this loop going to do?

for index in range(12):
	if index % 2 == 0:
		continue
	print(index)
	if index == 9:
		print('we are done')
		break
        
# 5. Using a Flag variable to stop iteration. 

items = [0, None, 0.0, True, 0.7]

found = False

for item in items:
    if item:
        found = True
        break
    if found:
        print('At least one item evaluates to true')
else:
    print('All items evaluate to False')


# 6. For loop over strings

phrase = 'alphabet soup'

for char in phrase:
	print(char)
	

for index in range(len(phrase)):
	print(index)



for index in range(len(phrase)): # another way to index a sequence
	print(phrase[index])
	
    
# 7. including indexing and enumerate


for index in range(len(phrase)):
	print(index, phrase[index])
	
for index, char in enumerate(phrase, 2): # gives us index and starts us at the 2nd second char of the phrase
	print(index, char)


# 9. Iterating over multiple sequences

name = 'Denver'
location = 'Colorado'

for position in range(len(name)):
    char_name = name[position]
    char_loc = location[position]
    print(char_name, char_loc)


# 10. This loop is trickier than it looks, what is going on? Try adding print(position, characters) before location line.

for position, characters in enumerate(range(len(name))):
    location = name[position]
    print(characters, location)
    
'''
The variable name is assigned the string 'Denver', which has a length of 6.

range(len(name)) generates a sequence of numbers from 0 to 5.

enumerate() takes this sequence and pairs each number with its own index. 
So, it produces the pairs (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), and (5, 5).

In the for loop, position is assigned the index from enumerate (0, 1, 2, 3, 4, 5) and characters 
is assigned the value from range (also 0, 1, 2, 3, 4, 5).

Inside the loop, name[position] accesses the character at that specific index in the string 'Denver'.

Finally, print(characters, location) prints the value of characters (the number from range) 
followed by the character from the name string that was just assigned to the location variable.
'''
    
# 11. Iterating over multiple lists with enumerate and zip

people = ['Sarah', 'Thomas', 'David', 'Susan']
ages = [9, 34, 67, 52]

for people, ages in zip(people, ages):
    print(people, ages)
    
# 12. Extending example 15 with enumerate

people = ['Sarah', 'Thomas', 'David', 'Susan']
ages = [9, 34, 67, 52]
locations = ['Idaho', 'Boston', 'Texas', 'Virginia']

for index, (people, ages, locations) in enumerate(zip(people, ages, locations)):
    print(f"{people} is {ages} years old and lives in {locations}.")


##### ASSIGNMENT EXPRESSION - THE WALRUS #####


'''Assignment expression syntax

name := expression

This does two things:

It assigns the result of expression to the variable name.

It returns the value of expression

'''

value = 15
mod = 6

remainder = value % mod

if remainder:
    print(f'Not divisible!  the remainder is {remainder}')
    

# assignment expression

if remainder := value % mod:
    print(f'Not divisible! The remainder is {remainder}')

# we might also see the walrus used in relation to a loop: here it is part of a conditional expression

while (variable := input(prompt) not in 'some data container you define')


##### WHILE LOOPS #####

'''
While loops as long as a condition is satisfied

There are various ways to code a while loop:

1. Basic
2. Infinite loop with a break
3. While loop with Else clause
4. Sentinal-controlled loop
5. Flag-controlled loop
6. Counter-controlled loop
7. Loop with multiple conditions
8. Loop with continue statement
'''


# 13. Initialization, condition, and update using a counter -- using a list 

people = ['Sarah', 'Thomas', 'David', 'Susan']
ages = [9, 34, 67, 52]

position = 0

while position < len(people):
    person = people(position)
    age = ages(position)
    print(person, age)
    position += 1


# 14. While / Else structure

a = 0

while a < 8:
	print('a is less than or equal to 7')
	a += 1
else:
	print('a is now more than 7')


# 15. Sentinal-controlled: loop until specific value is encountered

ending = 'stop'

data = input("Enter data (or 'stop' to finish): ")
while data != ending:
    print(f"Processing: {data}")
    data = input("Enter data (or 'stop' to finish): ")


# 16. Flag-controlled: loop based on a boolean condition (flag)

run = True

while run:
	text = input('Would you like to continue, yes or no?')
	if text = 'no':
		print(f'You said {text}....exiting program')
		break
	else:
		print('You said {text}. Great, lets go another round')
		

# 17. Conditional thresholds, break and continue statements

a = 0

while a < 10:
	if a == 7:
		print('You hit 7 that\'s a magic number')
		break
	print(a)
	a += 1


i = 0

while i <= 20 :
    i += 1
    if i % 2 == 1 :
        continue
    print(i)


# 18 Nested While Loops - review this using python_tutor.com. We can nest for loops as well.


outer = 0
while outer < 3:
    inner = 0
    while inner < 2:
        print(f"({outer}, {inner})")
        inner += 1
    outer += 1



# Example: Calculating the binary representation of an integer. We could also use bin

n = 39
remainders = []
while n > 0:
    remainder = n % 2 # will either be 0 or 1
    remainders.append(remainder)
    n //= 2 # floor division divide n by 2, shifts number to the right in binary
remainders.reverse()
print remainders


### Bonus: random(), isupper() - just for fun

import random

for x in range(5):
	y = random.randint(-10, 100)
	if y < 0:
		break
	else:
	print(y, 'no negative generated')
	
menu = 'SpaGetti and MeatBalls'

for letter in menu:
	print(letter)
	if letter.isupper():
		print'\nCapital Letter'

