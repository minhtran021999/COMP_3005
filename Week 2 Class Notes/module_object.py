

'''
I said previously that a .py file is essentially a text file. 
This changes when we load and run that file. 

# when we load a module we create two objects in the background

1. A module object - contains the module namespace (a dictionary that maps names
to objects) and attributes

2. A file object - for handling (reading/writing) files

Python assigns module attributes to every module when it is loaded. 

'''

# Example 1. Math module and associated namespace attributes


import math

print(f"\nMath module object: {math}")
print(f"\nMath module namespace type: {type(math.__dict__)}")

print("\nSome things in math's namespace:")

math_items = [(name, obj) for name, obj in math.__dict__.items() 
              if not name.startswith('_')][:]

for name, obj in math_items:
    print(f"  '{name}' -> {type(obj).__name__}")


# Here is an example of the __name__ attribute

print(f"\n\nI am a .py module. My __name__ is: {__name__}\n\n")

# Lets review all of the attributes

for name in sorted(dir()):
    print(f'{name}')

# The __builtin__ attribute provides access to Python functionality (functions, exceptions, and constants. 
# For example, print(), True, SyntaxError 

'''

Module Builtins Consist of the following:

Exceptions - e.g., Syntax Error
Warnings - DeprecationWarning
Constants - None, True, False
Data Types - bool, set, int, list
Functions - min, max
Decorators - e.g., class method, property
Magic Methods - eg. __name__
Interactive Helper Objects - e.g., exit
'''

# Let's see how many builtins there are

print(f"\n\nNumber of builtins: {len(dir(__builtins__))}\n\n")

# # Let's look at these builtins

print(f'These are our builtins:')

builts = dir(__builtins__)
for item in builts:
    print(item)


