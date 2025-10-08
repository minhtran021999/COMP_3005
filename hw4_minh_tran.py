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
#creating Vehicle class
class Vehicle:
    '''
    This is the Car class, containing its attribute data and methods as defined below:

    Attribute data:
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

    Attribute method:
        # "vehicle_range_miles": this method takes no arguments and returns a float which should be
        the total range (miles) of the vehicle. This method must work for either gas and electric engine types.
    '''

    #attribute data
    def __init__(self, color, year, make, model, engine_type, top_speed, mpg=None, tank_capacity=None, ev_efficiency=None, ev_capacity=None):
        '''
        Attribute data initiation
        '''
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.engine_type = engine_type
        self.top_speed = top_speed
        self.mpg = mpg
        self.tank_capacity = tank_capacity
        self.ev_efficiency = ev_efficiency
        self.ev_capacity = ev_capacity

    #attribute method
    def vehicle_range_miles(self):
        '''
        This method calculates the maximum range a vehicle can cover with a full tank of gas (engine_type: 'gas'),
        or when fully charged (engine_type: 'electric')
        '''
        if self.engine_type == 'gas':
            return self.mpg * self.tank_capacity
        else:
            return self.ev_capacity * self.ev_efficiency

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
 
 #create GasCar class inheriting from parent class Vehicle
class GasCar(Vehicle):
    '''
    This is GasCar class, inheriting from the parent class Vehicle

    Attribute data:
        # all attributes from Vehicle, plus:
        # num_doors (this includes the hatch/tail gate, int)

    Attribute methods:
        # change_color: this method takes in a color as an argument (str)
        # and change the color attribute of the Car instance

        # car_info: this method takes no arguments and return a string
        # with the basic car info in the format : "make - model - color - num_doors"

        # better_mileage: this method takes two instances of the Car
        # class and returns the car info, using the car_info method, of the car
        # instance that gets the better mileague - mpg or efficiency, depending on engine_type.

    '''
    #counter for instances created
    num_car = 0

    #attribute initiation
    def __init__ (self, color, year, make, model, engine_type, top_speed, mpg=None, tank_capacity=None,
                  ev_efficiency=None, ev_capacity=None, num_doors=None):
        '''
        Attribute initiation by calling the init method from the parent class Vehicle and pass in data,
        then creating new attribute called num_doors
        '''

        super().__init__(color, year, make, model, engine_type, top_speed, mpg, tank_capacity, ev_efficiency, ev_capacity)
        self.num_doors = num_doors
        GasCar.num_car += 1

    #attribute methods
    def change_color(self, color):
        '''
        This method changes the 'color' attribute of the instance
        '''
        self.color = color
        return self.color

    def car_info(self):
        return f'{self.color} - {self.make} - {self.model} - {self.num_doors}'

    def better_mileage(self, other):
        if self.vehicle_range_miles() > other.vehicle_range_miles():
            return self.car_info()
        else:
            return other.car_info()

    

if __name__ == '__main__':
    
    print("\n#### Exercise 1. ####\n")

    # put statements, expressions, and executable code here

    #(color, year, make, model, engine_type, top_speed, mpg, tank_capacity, ev_efficiency, ev_capacity)

    # 1.a: Create an instance of the Vehicle class called 'gas_vehicle' for a 1955, red, chevrolet, Bel Air, 
    # that has a top speed of 132 mph, with a 12 gallon capacity gas engine that gets 13.3 mpg. 
    gas_vehicle = Vehicle('red', 1955, 'chevrolet', 'bel air', 'gas', 132.0, 13.3, 12.5)

    # 1.b: Create an instance of the Vehicle class called 'electric_vehicle' for a 2025, silver, Tesla, 
    # Model 3, that has a top speed of 163 miles/kWh, an ev_capacity of 82.0, and an ev_efficiency of 4.2
    electric_vehicle = Vehicle('silver', 2025, 'tesla', 'model 3', 'electric', 163.0, None, None, 4.2, 82.0)

    # 1.c: Using f-string style and the instance attributes, print the gas_vehicle make, model, and mpg 
    print(f'gas_vehicle: \n make: {gas_vehicle.make} \n model: {gas_vehicle.model} \n mpg: {gas_vehicle.mpg} \n')

    # 1.d: Using f-string style and the instance attributes, print the electric_vehicle make, model, ev_capacity and ev_efficiency. 
    print(f'electric_vehicle: \n make: {electric_vehicle.make} \n model: {electric_vehicle.model} \n ev_capacity: {electric_vehicle.ev_capacity} \n ev_efficiency: {electric_vehicle.ev_efficiency} \n ')

    # 1.e: Calculate the gas_vehicle driving range on a full tank of gas using the associated instance method.
    print(gas_vehicle.vehicle_range_miles())


    print("\n#### Exercise 2. ####\n")

    # put statements, expressions, and executable code here
    
    #2.a - create three GasCar instances based on the following information.
    # the first car is a silver 4-door honda civic (2015) that gets 32.0 mpg and can reach 130 miles/hr. It has a tank capacity of 12.4 gal.
    # the second car is a 2008 ford mustang gt that's red and has two doors. It can reach up to 155 miles/hr on a 16.0 gal tank and gets 17.0 mpg. 
    # the third car is a Toyota Camry that's blue and was made in 2022. It has 4 doors. It also has a 15.8 gal tank and gets 32.0 mpg. It's top speed is 135.
    car1 = GasCar('silver', 2015, 'honda', 'civic', 'gas',130.0, 32.0, 12.4, None, None, 4)
    # print(car1.car_info())

    car2 = GasCar('red', 2008, 'ford', 'mustang', 'gas', 155.0, 17.0, 16.0, None, None, 2)
    # print(car2.car_info())

    car3 = GasCar('blue', 2022, 'toyota', 'camry', 'gas', 135.0, 32.0, 15.8, None, None, 4)
    # print(car3.car_info())

    #2.b - change the color of the first car to purple and verify the change using a print statement (f-string style).
    car1.change_color('purple')
    print(car1.color)
    
    #2.c - print out the make, model, color, and number of doors for the third car.
    print(car3.car_info())

    #2.d - determine whether the second car gets better mileage than the first car (use an instance method). 
    print(car2.better_mileage(car1))
    
    #2.e - determine the driving range of the third car
    print(car3.vehicle_range_miles())
    
    #2.f - calculate the total number of GasCars that have been created (3 pts)
    print(GasCar.num_car)
 