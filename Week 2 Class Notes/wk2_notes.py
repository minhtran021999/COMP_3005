#### WEEK 2. FUNCTIONS ####

'''
Quiz

1. Predict the following before running:

x = 0.1 + 0.1 + 0.1
y = 0.3

print(f"Are they equal? {x == y}")
print(f"x = {x:.17f}")
print(f"y = {y:.17f}")

2. What is the order in which the following calculations will be formed

final_rating = baseline_score + follow_up_score / 2 * num_sessions % 5      # (div, mult, modulus - eval left to right)>addition
final_rating = (baseline_score + follow_up_score) / 2 * num_sessions % 5    # paren > left to right or equal precendence (/, *, %)

------------------------------------------------------

1. Last week review
2. HW2 posted. Be aware of rounding errors on the last question. Better written as a list???
2. Learning Outcomes for this week
3. module object and file object
    - focus on __name__ builtin

4. Functions
    - syntax and conventions
    - callability - parameters, arguments
    - return statements
    - local and global scope - catching variables
    - Orchestration

    Functions: Reduce duplication, break complex tasks into smaller steps, hide implementation details, 
    improve traceability and readability

Modularity - enables iteration and reuse, etc. Programs are puzzles of
functions and classes.

Namespace - a mapping of names (identifiers) to objects (builtin, global, local, enclosing)

Scope - where in our program we have access to given variables. Global variables
are available throughout program. Local variable (inside function), available
only within function.

'''

##### FUNCTION CODING CHALLENGE #####

'''
Instructions: You need to create a simple function to calculate sales tax for different
purchase amounts. This will help you understand function structure and calling.

Define a function called 'calculate_sales_tax' that:
- Takes one parameter: purchase_amount
- Calculates tax at 8.5% rate
- Returns the tax amount (not the total)
- Include a docstring explaining what the function does

Test your function with these scenarios:
- Purchase of $50.00 (store result in 'tax_50')
- Purchase of $125.75 (store result in 'tax_125')
- Print both results with descriptive messages

****** POSSIBLE ANSWER ******

def calculate_sales_tax(purchase_amount):

    """
    Calculate sales tax on a purchase amount.
    
    Args:
        purchase_amount (float): The amount of the purchase
        
    Returns:
        The tax amount (float): percent of purchase
    """

    return purchase_amount * 0.085

  
tax_50 = calculate_sales_tax(50.00)  # argument: 50.00
tax_125 = calculate_sales_tax(125.75)  # argument: 125.75

print(f"Tax on $50.00: ${tax_50:.2f}")
print(f"Tax on $125.75: ${tax_125:.2f}")

'''

##### FUNCTION SYNTAX, CALLS, PARAMETERS, ARGUMENTS #####

'''
Convention - function syntax --> snakecase

parameters are defined in the function definition & arguments are what you pass
as the parameters - 'value' is the parameter below.

When we call or invoke the function, what we pass into it is the argument
e.g., square_integer(6)

function wont run without making a call -- we'll explore this.
'''

# Example 1. Minimal function

def minimal_function():
    '''
    Does nothing
    '''
    pass

# access list of attributes and methods

print(dir(minimal_function))


# # Example 1a. Call a function without arguments. Void Function - no return statement
#
def print_function(): # definition, name, parameter --> missing argument
    '''
    Prints default string
    '''
    print('\nDo Something Marvelous\n')
    return
#
print_function()
#
#
# # Example 2a. Calling a function with a positional arguments
#
def square_integer(value: int) -> int:
    '''
    Squares a single integer
    '''
    squared_value = value ** 2
    print(f'\nThe positional argument: {value} squared is equal to {squared_value}.')
    return squared_value # whats wrong here?

# Please experiment with the following. Comment out code that results an error when you are done

square_integer(6)  
#print(squared_value) #what happens?
#squared_value = square_integer(6)
#print(squared_value)
#print(square_integer.__annotations__) # compare your output to the function

# # Example 2b. Calling a function with a default parameter
#
def square_integer(value: int = 44):
    '''
    Squares integer and prints result
    '''
    squared_value = value ** 2
    print(f'\nThe default parameter: {value} squared is equal to {squared_value}.')
    return squared_value

val = square_integer()
print(val)


# # Example 2c. Combination of positional & Defaults, keyword arguments

def square_integer(weather, value = 44):
    '''
    Squares integer and prints result
    '''
    squared_value = value ** 2
    print(f'\nThe positional argument entered for our weather is: {weather}, bodes well for us')
    print(f'\nThe keyword argument: {value} squared is equal to {squared_value}.')
    return squared_value

square_integer('sunny', value = 2)

# # Example 2e. Multiple returns & unpacking

def return_multiple_outs(value1, value2, value3):
    '''
    Adds and multiplies numeric input
    '''
    value_sum = value1 + value2 + value3
    mult_values = value1 * value2 * value3
    return value_sum, mult_values

val_add, val_mult = return_multiple_outs(3,4,5)

print(val_add, val_mult)


##### ARGUMENT ORDER DURING FUNCTION CALL ##### 

# Example 3a - order of defaults doesnt matter, just after positional

def arg_function(a, c = 2, b = 4.5):
    '''
    Returns arguments
    '''
    return a, b, c
    
a, b, c = arg_function(5)
print(f'\nThe values of a, b, c are: {a}, {b}, {c}, respectively')

a, b, c = arg_function(5, b = 30, c = 0)
print(f'\nThe values of a, b, c are: {a}, {b}, {c}, respectively')


# Example 3b. Positional Wildcards

def wildcard(a, *args):
    '''
    Takes in any number of positional arguments and
    returns an average
    '''
    count = len(args) + 1
    total = sum(args) + a
    return (total/count)

avg = wildcard(2, 5, 7, 8)
print(f'The average of the inputs is: {avg}')

# Example 3c. Keyword Wildcards  **kwargs - experiment on your own
# kwargs is a dictionary to holds all the keywords passed to the function - .get() is a dict method
# we will learn about dictionaries in a future class

def multi_args(a, **kwargs):
    '''
    Accepts a positional argument and keyword arguments
    and returns a formatted string.
    '''
    mod1 = kwargs.get('mod1', '') # '' empty string default
    city = kwargs.get('city', '')
    sentiment = kwargs.get('sentiment', '')
    mod2 = kwargs.get('mod2', '')

    return f'{a} {mod1} {sentiment} {mod2} {city}'

combined_inputs = multi_args('The weather', mod1="is", city="Boulder", sentiment="great", mod2="in")

print(combined_inputs)

##### LOCAL AND GLOBAL SCOPE #####


# Example 4a. - global and local variables --> immutable, show this in python tutor.com


var1 = 45

def scope_comparison():
    '''
    Prints and returns local string and int var
    '''
    
    var1 = 'Bugs Bunny'
    var2 = 1
    
    print(f'Local var1 value: = {var1} and local var2 value: = {var2}.')
    return var1, var2

scope_comparison()

print(var1)


# Example 4b. - global and local variables --> mutable obj; side effect
# We are using a list in this example. We'll learn more about this data structure in a future class

var1 = [45] # lists are mutable

def return_greater():
    '''
    Mutates list and returns list and int var
    '''
    
    var1[0] = 'Road Runner' # assignment vs. mutation; not creating a new local var
    var2 = 1

    return var1, var2

return_greater()

print(var1)



# Example 4c. Using global in the local scope


def global_scope():
    '''
    Creates but does not return global var
    '''

    global global_var # syntax to create a global var within the local scope

    global_var = "Global var in local scope"

global_scope()

print(global_var)



##### Docstrings #####

#Example 5a. keyword without return

def default_print(some_docstring = "\nWe're learning about default values."):

    '''
    Prints default value unless replaced by passing keyword arg

    args:
        some_docstring (str): default value

    returns:
    None
    '''

print(default_print())

# Example 5b. positional and keyword with return

# There are often individual conventions that organizations dictate for docstrings.These might include tests to ensure proper behavior of the function (COMP3006)
         
# Example 5b. variable b is a default

def annotated(a: int = 4, b: int = 3) -> int: 
    '''
    Calculates the product of a positional argument and default
    argument and returns an integer

    Args:
        a (int)
        b (int)

    returns:
        (int): product of a and b
    '''
    return a * b

print(annotated())
print(annotated.__doc__)
print(annotated__)


###### HELPER FUNCTIONS ######

'''
Helper functions (performs a subtask) are used by another function. They are considered 'private'.
This is indicated by a leading underscore.
'''

# Example 6. Temperature conversion

def _farenheit_to_celcius(farenheit: int):
    return round((farenheit -32) * (5/9), 2)

def _celcius_to_farenheit(celcius: int):
    return round((celcius / (5/9) + 32), 2) # round to two decimal places

def convert_temperature(temp: int, current_scale: str):
    
    '''
    Takes helper functions and converts temperature to farenheit or celcius
    depending on the unit of measurement for the input. It returns a float value
    in the alternate scale.
     
    args:
        temp (int) - actual temperature 
        current_scale (str) - the scale entered (celcius or farenheit)
    
    returns:
        (int): temperature converted to alternate scale
    
    '''
    if current_scale.lower() in ('farenheit', 'f', 'farenheit'):
        return _farenheit_to_celcius(temp)
        
    else:
        return _celcius_to_farenheit(temp)

print(f"The converted temperature is {convert_temperature(53, 'Farenheiht')}")





