'''
COMP 3005
Homework 4 - Python Classes (Object Oriented Programming)

Concepts covered: class constructor, class instances, class vs instance attributes & methods, main orchestrator

General Homework Guidelines: 
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing. 
- Use a consistent coding style. 
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs. 
- Every function must include a docstring for documentation (see: 
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - input parameters, their types and what they are for
     - return data type and what it is

- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
  
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.


Homework 4 Instructions:
1. Every class, method and function must have proper DocString documentation of the
following form :

def someFunction(arg1, arg2):
    """
    Function DocString. Indent the DocString.
    One or two lines explaining what the function does

    Args:
        arg1 (type): what is this argument
        arg2 (type): what is this argument

    Return:
        (type): what is being returned by the function ?
    """
    #your code here


class SomeClassIMadeUp:
    """
    Class DocString. Indent the DocString
    One or two lines explaining what the class does

    Attributes:
    ----------------------------------------
        attr1 (type): what is this attribute
        attr2 (type): what is this attribute

    Method:
    ----------------------------------------
        method1: what does this method do
        method2: what does this method do
    """

    def method_inside_class(arg1, arg2):
        """
        Method DocString. Indent the DocString
        One or two lines explaining what the method does

        Args: (don't include 'self' in the arguments)
            arg1 (type): what is this argument
            arg2 (type): what is this argument

        Return:
            (type): what is being returned by the method ?
        """

#### HOMEWORK 4 Guidance ####

1. This homework consists of two exercises that each have multiple parts

2. For this homework you can use Python's min() and max() built-in functions to set a range. No imports are required. 
    
    Example 1.a. max(value1, value2) -> returns the larger of two values, min does the opposite
    
    Example 1.b. max(val1, min(val2, val3)): nested function keeps a value within a given range  
        -> inner function (min(val2, val3)) returns smaller of v2 and v3,
        -> outer function evaluates max(val1, result from first step) -> which ensures that the value doesnt
        go below val1

        given: max(3.0, min(5.0, 6.5)) ->returns 5.0 capped at upper bound
        given: max(3.0, min(5.0, 1.5))  -> returns 3.0 capped at lower bound

3. Class attributes are not included in the __init__() constructor. The latter is used to bind attributes (data)
    to the instance when the class is called. 

4. Use the if __name__ == '__main__': orchestrator to execute all code (e.g., print statements, method/attribute calls, etc.)

5. If you want to experiment with basic error handling, you can use the "raise" keyword with if/else statements (no HW points associated with this).
    See: https://www.geeksforgeeks.org/python/python-raise-keyword/
    
    for example:    If something:
                        do something
                    else:
                        raise SomeException("string that will print the error as you describe it"). Common exceptions include: ValueError, ZeroDivisionError, TypeError 
'''
#--------------------------------------------------------------------------#



##### Exercise 1: multiple parts 

# Make a class called Vehicle, that contains an __init__ method for the following attributes (15 pts):
# color (str)
# year (int)
# make (str)
# model (str)
# top_speed in miles/hour (float)
# mpg (miles per gallon, float)
# engine_type (gas, electric) (str)
# tank_capacity (gal)
# ev_capacity (kWh) -- between 50 & 100
# ev_efficiency (miles/kWh) -- between 3 & 5

'''
The Vehicle class must also contain the following method (10 pts):

"vehicle_range_miles": this method takes no arguments and returns a float which should be
    the total range (miles) of the vehicle. This method must work for either gas and electric engine types.

The following are (3 pts) each

    1.a: Create an instance of the Vehicle class called 'gas_vehicle' for a 1955, red, chevrolet, Bel Air, 
    that has a top speed of 132 mph, with a 12 gallon capacity gas engine that gets 13.3 mpg. 

    1.b: Create an instance of the Vehicle class called 'electric_vehicle' for a 2025, silver, Tesla, 
    Model 3, that has a top speed of 163 miles/kWh, an ev_capacity of 82.0, and an ev_efficiency of 4.2
    
    #### For 1.c and 1.d you need to know how to access the instance attributes. All print statements and other code executions  ####

    1.c: Using f-string style and the instance attributes, print the gas_vehicle make, model, and mpg 

    1.d: Using f-string style and the instance attributes, print the electric_vehicle make, model, ev_capacity and ev_efficiency. 

    1.e: Calculate the gas_vehicle driving range on a full tank of gas using the associated instance method.
'''


##### Exercise 2. - multiple parts 

# Create a 'GasCar' class that inherits from Vehicle (10 pts).

# The class must have the following attributes :
# -color (str)
# -year (int)
# -make (str)
# -model (str)
# -num_doors (this includes the hatch/tail gate, int)
# -engine_type (gas, diesel, electric) (str)
# -top_speed in miles/hour (float)
# -mpg (miles per gallon, float)
# -tank_capacity (gallons or Kwh, float)

# Include a class attribute, called num_cars, which increases every time
# a new Car instance is created (5 pts). 

# Create the following methods (5 pts each):

    # change_color: this method takes in a color as an argument (str)
    # and change the color attribute of the Car instance

    # car_info: this method takes no arguments and return a string
    # with the basic car info in the format : "make - model - color - num_doors"

    # better_mileage: this method takes two instances of the Car
    # class and returns the car info, using the car_info method, of the car
    # instance that gets the better mileague - mpg or efficiency, depending on engine_type.

# The following are 5 pts each unless otherwise specified

#2.a - create three GasCar instances based on the following information.
    # the first car is a silver 4-door honda civic (2015) that gets 32.0 mpg and can reach 130 miles/hr. It has a tank capacity of 12.4 gal.
    # the second car is a 2008 ford mustang gt that's red and has two doors. It can reach up to 155 miles/hr on a 16.0 gal tank and gets 17.0 mpg. 
    # the third car is a Toyota Camry that's blue and was made in 2022. It has 4 doors. It also has a 15.8 gal tank and gets 32.0 mpg. It's top speed is 135.
 #2.b - change the color of the first car to purple and verify the change using a print statement (f-string style).
 #2.c - print out the make, model, color, and number of doors for the third car.
 #2.d - determine whether the second car gets better mileage than the first car (use an instance method). 
 #2.e - determine the driving range of the third car
#2.f - calculate the total number of GasCars that have been created (3 pts)
 
 

if __name__ == '__main__':
    
    print("\n#### Exercise 1. ####\n")

    # put statements, expressions, and executable code here

    print("\n#### Exercise 2. ####\n")

    # put statements, expressions, and executable code here
    
    

 