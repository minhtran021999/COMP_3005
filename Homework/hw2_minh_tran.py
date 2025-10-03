'''
COMP 3005
Homework 2 - Functions & Variable Scope

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
  enclosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.

Homework 2 Instructions:
You should submit two .py files, this file and a new file you create for problem 6 called : extra_functions.py.

'''
#--------------------------------------------------------------------------#


# 1. Create a function called seconds_to_hms that takes an argument `seconds`, 
# an integer number of seconds, and returns a string in the format "xx h, xx m, xx s", 
# where xx is the number of hours, minutes and seconds. This is turning the question 
# from last week's homework into a function. (15 points)

def seconds_to_hms(seconds):
	'''
	Converts a given number of seconds into hours, minutes, and seconds format

	Parameters:
	seconds (int): The total number of seconds to be converted

	Returns:
	str: A string representing the time in "xx h, xx m, xx s" format
	'''
	hrs = seconds // 3600
	mins = (seconds % 3600) // 60
	secs = seconds % 60
	return f"{hrs} h, {mins} m, {secs} s"

print(f'1 The result is: {seconds_to_hms(3665)}')  #Test


# 2. Create two functions called miles_to_km and km_to_miles. Each function takes one
# parameter, distance, of type float. Each function will convert the distance into 
# either miles or kilometers based on the function used and return that value. 
# (15 points)
# 1 mile = 1.6 kilometers
# 1 kilometer = 0.62 miles

def miles_to_km(distance: float):
	'''
	Converts a distance from miles to kilometers

	Parameters:
	distance (float): The distance in miles to be converted

	Returns:
	float: The equivalent distance in kilometers
	'''
	return distance * 1.6

def km_to_miles(distance: float):
	'''
	Converts a distance from kilometers to miles

	Parameters:
	distance (float): The distance in kilometers to be converted

	Returns:
	float: The equivalent distance in miles
	'''
	return distance * 0.62

print(f'2 10 miles equal to {miles_to_km(10)} kilometers')  #Test
print(f'2 10 kilometers equal to {km_to_miles(10)} miles')  #Test


# 3. Create a function called europe_US that takes 2 parameters, sqm_to_sqft and euro_to_dollars, 
# both of type float. The function must return the coverted values as a tuple: sqft, dollars. 
# This will allow us to convert real state listings in Europe, which are in metric, to imperial 
# units so we can shop for our next vacation home. (10 points)
# 1 sqm = 10.7639 sqft
# 1 euro = 1.08 dollars

def europe_US(sqm_to_sqft: float, euro_to_dollars: float):
	'''
	Converts square meters to square feet and euros to dollars

	Parameters:
	sqm_to_sqft (float): Square meters to be converted
	euro_to_dollars (float): Euros to be converted

	Returns:
	tuple: a tuple containing converted square feet and US dollars
	'''
	sqft = sqm_to_sqft * 10.7639
	dollars = euro_to_dollars * 1.08
	return sqft, dollars

result1, result2 = europe_US(15, 20)  #Test
print(f'3 50 sqm equal to {result1} sqft & 100 euros equal to {result2} dollars')

# 4. Create a function called road_trip that takes 1 parameter, mpg (miles per gallon), of type float. 
# The function should ask for user input on how far they intend to drive on their road trip. Once 
# you have the distance, calculate the number of gallons they will need to complete the road trip. 
# Use $3.07 as the average cost of a gallon of gas. Return the total cost of gas for the road trip. 
# (15 points)

def road_trip(mpg: float):
	'''
	Calculates total cost of gas for a road trip based on mpg and distance driven
	
	Parameters:
	mpg (float): Miles per gallon of the vehicle

	Inputs:
	Distance (float): Distance to be driven in miles
	
	Returns:
	float: Total cost of gas for the road trip
	'''
	distance = float(input('Please enter the distance you plan to drive (in miles): '))
	gallons_needed = distance / mpg
	cost_per_gallon = 3.07
	total_cost = gallons_needed * cost_per_gallon
	return total_cost
print(f'4 The total cost of gas for the road trip is: ${road_trip(30):.2f}')  #Test


# 5. Create a function called insulate_home_cost that takes no parameters and asks the user to input 
# the length, width and height of the the basement of their house. Once you have these values,
# calculate the surface area (sq ft) of each side of the basement and use $2.75 as the average cost 
# of spray foam insulation per sq ft. Once you have that value multiply. Return the total insulation 
# cost. (15 points)

def insulate_home_cost():
	'''
	Calculates the total cost of insulating a home's basement based on provided dimensions

	Parameters:
	None

	Inputs:
	Length (float): Length of the basement in feet
	Width (float): Width of the basement in feet
	Height (float): Height of the basement in feet

	Returns:
	Total cost of insulation (float)	
	'''

	length = float(input('Please enter the length of the basement in feet: '))
	width = float(input('Please enter the width of the basement in feet: '))
	height = float(input('Please enter the height of the basement in feet: '))
	surface_area = (length * height) * (width * height) * 2 # Only walls, no floor or ceiling
	cost_per_sqft = 2.75
	total_cost = surface_area * cost_per_sqft
	return total_cost
print(f'5 The total cost of insulating the basement is: ${insulate_home_cost():.2f}')  #Test
	

# 6. We're going to practice importing functions from another file. Complete the following steps:
#  - Create a new .py file called extra_functions.py
#  - In extra_functions.py, write a function called midpoint which takes an integer as input and returns 
#    the midpoint between that integer and 0.
#  - Include an if __name__ == '__main__' codeblock in extra_functions.py to test your midpoint function.
#  - Import extra_functions.py into this file.
#  - Run this line of code: midpoint_of_10 = midpoint(10)
# (20 points)

from extra_functions_hw2_minh_tran import midpoint
midpoint_of_10 = midpoint(100)
print(f'6 The midpoint between 10 and 0 is: {midpoint_of_10}')  #Test

# 7. Fix the following code (10 points)

def BMI(height, weight):
	'''
	Calculates the Body Mass Index (BMI) based on height and weight

	Parameters:
	height (float): Height in inches
	weight (float): Weight in pounds

	Returns:
	float: The calculated BMI
	'''

#Calculate BMI

	BMI = (weight / (height ** 2)) * 703

	return BMI

print(f'7 Your BMI is: {BMI(68, 170):.2f}')  #Test
	
	
	


