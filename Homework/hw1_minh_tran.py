'''
COMP 4401
Homework 1 - Variables & Boolean Expressions

General Homework Guidelines:

- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 

Homework 1 Guidelines:

- For questions 1-4, solve without using python to ensure you understand data types and 
  boolean expressions. You can then verify your answers using python.
- Responses to questions 1-4 should be included in Python script files using inline comments 
  (# comment) or multiline comments using triple quotes. 

'''
#--------------------------------------------------------------------------#

# 1. For each of the following expression, identify the data type and value (10 points):
# A) 5+3/5*(4-10)

print('1a The value of 5+3/5*(4-10) is:', 5+3/5*(4-10))
print('1a The datatype is', type(5+3/5*(4-10)).__name__) # float

# B) 17//3**4 

print('1b The value of 17//3**4 is:', 17//3**4)
print('1b The datatype is', type(17//3**4).__name__) # int

#--------------------------------------------------------------------------#

# 2. Evaluate the following boolean expressions (10 points):
# A) 15 % 4 < 20/3 

print('2a The value of 15 % 4 < 20/3 is:', 15 % 4 < 20/3) # True

# B) False or not (False or True) and True 

print('2b The value of False or not (False or True) and True is:', False or not (False or True) and True) # False

# C) 3/4==0 or 5<6

print('2c The value of 3/4==0 or 5<6 is:', 3/4==0 or 5<6) # True

#--------------------------------------------------------------------------#

# 3. Let a = True, b = True, c = False. Evaluate the following (15 points):

a = True 
b = True
c = False

# A) a and not b 
print('3a The value of a and not b is:', a and not b) # False
# B) b or c
print('3b The value of b or c is:', b or c) # True 
# C) not b == c
print('3c The value of not b == c is:', not b == c) # True 
# D) a and not c 
print('3d The value of a and not c is:', a and not c) # True
# E) b or c and not a  
print('3e he value of b or c and not a is:', b or c and not a) # True
# F) a != b or b != c 
print('3f The value of a != b or b != c is:', a != b or b != c) # True

#--------------------------------------------------------------------------#

# 4. Select all invalid variable names below and give reason the variable name is 
# invalid (15 points):
# A) speed Of Light 
# B) x_2 
# C) 3Attempts 
# D) vertical-distance  
# E) B5V 

print('4a Invalid - variable contains space') # A) Invalid - contains space 
print('4b Invalid - variable starts with a number') # C) Invalid - starts with a number
print('4c Invalid - variable contains hyphen') # D) Invalid - contains hyphen

#--------------------------------------------------------------------------#

# 5. Write code that: initializes a variable to store the length of a square in inches, 
#    calculates the perimeter and area of the square, and prints the results. Test the 
#    program by changing the initial value for length to different integer values 
#    (15 points).

length = 15 # length of the square in inches
perimeter = 4 * length # calculating the perimeter
area = length ** 2 # calculating the area
print(f'5 The perimeter of the square is: {perimeter} inches') # printing the perimeter
print(f'5 The area of the square is: {area} square inches') # printing the area


# 6. Write code that will assign a variable to a given number of seconds and then 
#    calculate the equivalent number of hours, minutes and seconds. For example, 
#    300 seconds is 0 hours, 5 minutes and 0 seconds while 4503 seconds is 1 hour, 
#    15 minutes and 3 seconds. Assign separate variables to each of these values 
#    (i.e., hours, minutes, seconds). Evaluate your program calculations using different 
#    starting times (initial seconds). To be mindful of possible rounding errors, use
#    integers only (15 points).

total_secs = input('Insert desired number of seconds: ') # given number of seconds
total_secs = int(total_secs) # converting input to integer

hrs = total_secs // 3600 # calculating hours
secs_left = total_secs % 3600 # remaining seconds after calculating hours

mins = secs_left // 60 # calculating minutes
secs = secs_left % 60 # calculating remaining seconds

# printing the result
print(f'6 {total_secs} seconds is equivalent to {hrs} hours, {mins} minutes and {secs} seconds') 

# 7. Complete the following code so that when executed, it greets a user and asks the user
# for their age and height. It then evaluates whether the user meets height and weight criteria that 
# allows her/him to get on a carnival ride. Per policy, the user must be older that 12 years of age and at least 
# 50 inches tall to take the ride. Finally, the code prints out a determination that indicates to the user (by name) 
# whether or not she/he meets the criteria and can get on the ride. Note that the starter code may/may not 
# require correction in order to execute properly (10 points):

name = input("Greetings! What's your name? ")

min_age = input(f'Hi {name}, Please enter your age: ')
min_age = int(min_age)

min_height = input('... And nơw your height in inches: ')
min_height = int(min_height)

if min_age > 12 and min_height >= 50:
    print(f'7 You meet the age and height requirements and can get on the ride! Yeeeee haw!')

else:
    print(f'7 Sorry mate, you do not meet the age and/or height requirements and cannot get on the ride.')


#Complete the remaining code

# 1st_name = 
# height = 
# age = 

# 8. Given the four name bindings below, decide whether or not the data type (i.e., of the value) as written is an appropriate 
# type to use. Base the latter on the reference name, which provides an indication of what the value represents, and how 
# we typically communicate that value in day-to-day use. If you feel the data type is not appropriate, write code to cast it
# to a more appropriate type. For each entry, write a print statement that, when executed, provides a user with your rationale
# for keeping or changing the data type as well as the new value if altered. 

# Example: speed = '57' (miles per hour). The value is a string. We usually report speed as a whole number. Therefore it makes
# sense to cast the value to an integer. We might code the following: 

# print(f'Speed is typically reported as a whole number. \
#   Therefore it is more appropriate to cast the value and an integer. \
#   The new value is {int(speed)}.')

# Note: The backslash (\) is a line continuation character in the provided Python code. 
# Here it allows you to break a single logical line of code into multiple physical lines for improved readability 
# without changing the code's functionality.


age = 32.4
avg_height = float("73.54")
num_of_guests = int(47.0)
outside_temp = 73.2

print(f'8 Age is typically reported as a whole number. \
      Therefore it is more appropriate to cast the value as an integer. \
      The new value is {int(age)}.')

print(f'8 Average height is typically reported with decimal places. \
      Therefore it is more appropriate to keep the value as a float. \
      The value is {avg_height}.')

print(f'8 Number of guests is typically reported as a whole number. \
      Therefore it is more appropriate to cast the value as an integer. \
      The new value is {num_of_guests}.')

print(f'8 Outside temperature is typically reported with decimal places. \
      Therefore it is more appropriate to keep the value as a float. \
      The value is {outside_temp}.')







