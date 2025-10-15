
##################################
### Week 5. Exception Handling ###
##################################


'''
Exception handling is a means to find and manage specific errors so that the program can continue running in the 
presence of such errors. Exception handling is not a substitute for good code and should be employed sparingly!!

Exception handling can be designed for those errors that are likely to occur as well as those that are unexpected.

Learning Outcomes - you should be able to:
	- define an 'exception' - errors that arise during program execution
	- understand when/how to use try/except to mitigate script failure due to errors
    - write code for single and multiple exceptions
    - create user defined exceptions
    - include 'finally' statements in your code to complete a last task before the try statement is complete 

For detailed information see: https://docs.python.org/3/tutorial/errors.html
'''


############################################################################### 

# Example 1. 

# The following program will crash (script will stop running) due to a Type Error

while True:
    print(2 + '2') # results in a Type Error
    print('This should print as true without an error') #this wont run
    break

############################################################################### 

# Example 2.  TRY/EXCEPT - comparable to elif statements. The following program manages the TypeError

# Note: query Google or Chatgpt to learn how to read a stack trace (error output in your terminal)


while True: 
    try:
        print(2 + '2')

    except TypeError as e: # catch error, e is an object alias, similar to a conditional statement
        print('There is a TypeError. Are both values numeric?')
        print(f'The stack trace message is: {e}')# e is an alias/var assigned to the exception. It represents a specific exception object

    except ValueError as v: # program will crash if we comment out the TypeError exception because there is no value error and the TypeError isnt addressed
        print(f'The stack trace message is: {v}')
    
    print('\nThis printed despite the TypeError!')
    break

# Example 3. Control Variable with exceptions

# An alternative way to to exit the loop through the use of a control variable. The latter acts as a flag that determines whether to continue looping until successful. Example 2 is more idomatic of python


control = True
while control:
    try:
        user_input = input("Enter a number: ")
        result = int(user_input)  # Try to convert to int
        print(f"Success! You entered: {result}")
        control = False  # Exit loop on success
    except ValueError as e:
        print(f"That's not a valid number. Try again. Error: {e}")
        # control stays True, so loop continues


############################################################################### 
# Example 4. Reading files - FileNotFoundError - Results if file in wrong directory or file doesn't exist.

# Note: try executing the following try/except using a .txt or .csv file in your working directory

filename = 'this_file_doesnt_exist.csv'
#filename = 'Short_dictionary.txt'

try:
	with open(filename, 'r') as file:
		data = file.readlines() # list of strings
		print(data)

except FileNotFoundError as e:
	print(f'There is a problem locating the file. Please check your filename: {e}')


# Example 4. Using with a while loop and user input to manage FileNotFoundError

while True:  # while allows prompt until correct file/directory is identified
	filename = input('enter a filename ')
	try:
		with open(filename, 'r') as file:
			data = file.readlines()
			print(data)
			break
		
	except FileNotFoundError as e:
		print(f'Error: {e}')
		print('Please enter a valid filename')
    
############################################################################### 
# Example 5. Raising Errors


# Create an error when something happens that you wish to avoid. Good for addressing values beyond a certain range that might not cause errors otherwise. 

response = int(input('please enter a positive integer < 20'))

print(f'The value you entered is: {response}.')

if (response < 0 or response >= 20):
	raise ValueError('Your entry is out of range.')
else: 
	print(f'Your value, {response}, is a wonderful choice.')
    
# let's put this into a function

def get_val():
    try:
        response = int(input('Please enter a positive integer < 20: '))
        if response < 0 or response >= 20:
            print(f'The value you entered is: {response}.')
            raise ValueError('Your entry is out of range.')
        else:
            print(f'The value you entered is: {response}. That is an appropriate choice.')
    except ValueError as e:
        print(e)
    print('Hello or anything else you would like to say')

get_val()


	
'''
The raise statement allows us to force a specific exception to occur. The sole argument in raise indicates the exception to be raised. 

This code intentionally raises a ValueError with the message “Hi there” using the raise statement within a try block. 
Then, it catches the ValueError exception, prints “An exception,” and re-raises the same exception using raise. 
This demonstrates how exceptions can be raised and handled in Python, allowing for custom error messages and further exception propagation.

'''


############################################################################### 
# Example 6. Multiple Exceptions & "finally" - has the advantage of covering a wide range of errors with the downside being a loss of specificity. 

import random as r # using a Python package for random number generation

def multiple_error(): 
 
    numerator = r.randint(1, 100) # selects a random integer between 1 - 100

    while True:
        try:

            input_value = input(f'\nEnter an integer value that is nonzero to divide {numerator}: ')
                 
            denominator = int(input_value)

            result = numerator / denominator
            
            print(f'The result is: {result}')
            

        except (ValueError, ZeroDivisionError) as error:

            print(f'Error: Invalid input. The stack trace indicates {error}. Please try again.')

        # loop continues
            
        # This second exception is a catch all for any other errors.
        except Exception as e:
            print(f'There is an error. The stack trace indicates {e}.')
            input_value = input('enter an integer value that is nonzero ')
        else:
            break
        
        # with try--except---finally, the latter executes whether or not an exception is raised.
        
        finally:
            print('You are exiting the exception handler') # excutes after try/except is complete
            
multiple_error()

############################################################################### 
# Example 6. Putting it all together in a function!

# This is a good example to study

def division_error_check():
	try:
		response = int(input('please enter a positive integer < 20 '))
		try:
			if response in range(1, 21):
				num = 43
				div = num/response
				return print(f'{43} divided by {response} = {div}')
			else:
				raise ValueError('The value you input is out of range')
		except ZeroDivisionError as z:
			print(f'There is an error in this code. The stack trace indicates: {z}')
	except ValueError as v:
		print(f'There is an input error in this code. The stack trace indicates: {v}')
	finally:
		print('The program has stopped running')

division_error_check()
