'''
COMP 3005
Homework 3 - Control Flow Statements

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
'''
#--------------------------------------------------------------------------#

# 1. Create a function distance_conversion that takes in two parameters, distance (float) and unit (string). 
# For the given unit type, "metric" or "imperial", your function will convert distance into miles or kilometers, respectively. 
# Note that distance_conversion should accomplishe the same outcome(s) as the two function you wrote for Q2 in homework 2. 
# (10 points)

def distance_conversion(distance, unit):
    
    """
    Convert distance between miles and kilometers based on the specified unit

    Parameters:
    distance (float): The distance value to be converted
    unit (str): The unit type, either "metric" for kilometers or "imperial" for miles

    Returns:
    float: The converted distance
    """

    if unit == "metric" and type(distance) == float:
        # Convert kilometers to miles
        return distance * 0.621371
    elif unit == "imperial" and type(distance) == float:
        # Convert miles to kilometers
        return distance / 0.621371
    else:
        return "Error: Invalid input. Please enter a float for distance, and 'metric' or 'imperial' for unit."

# print(distance_conversion(10.0, "metric"))  #Test metric
# print(distance_conversion(6.21, "imperial"))  #Test imperial
# print(distance_conversion(6, "metric"))  #Test invalid distance
# print(distance_conversion(10, "burgers"))  #Test invalid unit
# print(distance_conversion(10, 1))  #Test invalid unit type
# print(distance_conversion("ten", "imperial"))  #Test invalid distance type

#----------------------------------------------------------------------------------#

# 2. Create a function named build_wall that determines if a wall can be built to an exact length.
# The function should take three positive integer parameters:wall_length: The desired total length of the wall.
# small_brick_length: The length of the small bricks. large_brick_length: The length of the large bricks.
# You have an unlimited supply of both small and large bricks. The function must return True if it's 
# possible to build a wall of the exact wall_length, and False otherwise. 

def build_wall(wall_length:int, small_brick_length:int, large_brick_length:int):
    """
    Determine if a wall can be built to an exact length using small and large bricks. Winter is coming

    Parameters:
    wall_length (int): total length of the wall
    small_brick_length (int): length of small bricks
    large_brick_length (int): length of large bricks

    Returns:
    bool: True if the wall can be built to exact wall_length, False if not
    """

    if type(wall_length) != int or type(small_brick_length) != int or type(large_brick_length) != int:
        return "Error: All inputs must be integers"
    if wall_length < 0 or small_brick_length <= 0 or large_brick_length <= 0:
        return "Error: wall_length must be non-negative and brick lengths must be positive"

    for large_count in range(wall_length // large_brick_length + 1):
        remaining_length = wall_length - (large_count * large_brick_length)
        if remaining_length % small_brick_length == 0:
            return True
        else:
            return False

# print(build_wall(-10, 2, 3))  #Test non-negative wwall_length
# print(build_wall(10, -2, 3))  #Test positive small_brick_length
# print(build_wall(10, 2, -3))  #Test positive large_brick_length
# print(build_wall(10.5, 2, 3))  #Test integer wall_length
# print(build_wall(10, 2.5, 3))  #Test integer small_brick_length
# print(build_wall(10, 2, 3.5))  #Test integer large_brick_length
# print(build_wall(10, 1, 2))  #Test True
# print(build_wall(11, 2, 4))  #Test False

#----------------------------------------------------------------------------------#


# 3. Write a function, called calc_sum, that takes 3 integer values as arguments: a, b and c. The function 
# must return their sum. However, if one of the values is a duplicate, the duplicate value does not count 
# towards the sum. You cannot use the built-in method sum().

# For example 2, 4, 5 returns 11. The inputs 2, 2, 5 returns 7 and the inputs 1, 1, 1 returns 1. 
# (10 points)

def calc_sum(a, b, c):
  """
  Calculate the sum of three integers, excluding duplicates

  Parameters:
  a (int): First integer
  b (int): Second integer
  c (int): Third integer

  Returns:
  int: The sum of the integers, excluding duplicates
  
  *** Cannot use sum() ***
  """

  inputs = [a,b,c]

  og = set()
  dup = set()

  for num in inputs:
    if num in og:
      dup.add(num)
    else:
      og.add(num)

  sum = 0

  if type(a) != int or type(b) != int or type(c) != int:
    return "Error: All inputs must be integers"
  elif a != b != c:
    return a+b+c
  else:
    for num in og:
      sum += num
    return sum

# print(calc_sum(1,2,3))  #Test a,b,c all different 
# print(calc_sum(7,7,13)) #Test a,b same
# print(calc_sum(8,8,8))  #Test a,b,c same
#----------------------------------------------------------------------------------#

# 4. Create a function, called change_data_type, that takes in 4 parameters, int_val, str_val, float_val, and 
# float_val2. Check that each parameter is of the corresponding type, int, string, float and float 
# respectively. If their data type does not match these types, cast them to the right data type. Then 
# return all 4 values as a tuple. return (int_val, str_val, float_val, float_val2)
# (10 points)
#----------------------------------------------------------------------------------#

def change_data_type(int_val, str_val, float_val, float_val2):
  '''
  Check each of the input to see if they are the right data type respectively: int, str, float, float
  If not, cast them as such accordingly

  Parameters:
  int_val: datatype as int
  str_val: datatype as str
  float_val, float_val2: datatype as float

  Returns:
  tuple: contains all 4 values in the right datatype - (int_val, str_val, float_val, float_val2))
  '''

  result = list()
  try:
  #int_val
    if type(int_val) != int:
      int_val = int(int_val)
      result.append(int_val)
    else:
      result.append(int_val)

  #str_val
    if type(str_val) != str:
      str_val = str(str_val)
      result.append(str_val)
    else:
      result.append(str_val)

  #float_val
    if type(float_val) != float:
      float_val = float(float_val)
      result.append(float_val)
    else:
      result.append(float_val)

  #float_val2
    if type(float_val2) != float:
      float_val2 = float(float_val2)
      result.append(float_val2)
    else:
      result.append(float_val2)

    return result

  #in case int_val, float_val or float_val2 are inputed as strings, not all strings can be converted into int or float
  #example: str->float: "1" -> 1, but "lannister" -> error
  except Exception as e:
    return "Unable to cast input(s) to the designated datatype"

# print(change_data_type(15, 'winterfell', 1.6, 2.5)) #Test all inputs are in the RIGHT datatypes
# print(change_data_type(9.6, 13, 6, 8))  #Test all inputs are the in WRONG datatypes
# print(change_data_type(1.5, 15, 2, 'baratheon')) #Test wrong type but cannot convert (str->float)


# 5. Create a function, called change, that takes an input, cash (a float), and determines 
# the least number of dollar bills and coins needed for change. Note that bills are: 1, 5, 10, 20, 50, and 100.
# Coins can be: 1 cent, 5 cents, 10 cents and 25 cents (penny, nickel, dime, quarter). 
# (15 points)
# Example:
# If the dollar amount is 35.63, then your function should return the string:
# "1 x $20 bill, 1 x $10 bill, 1 x $5 bill, 2 quarters, 1 dime, 3 pennies"

import math
def change(cash:float):
  bills = [100, 50, 20, 10, 5, 1]
  coins = [0.25, 0.10, 0.05, 0.01]

  bills_change = math.floor(cash)
  #print(bills_change)

  coins_change = round(cash - bills_change, 2)
  #print(coins_change)

  result = list()

print(change(35.63))  #Example

#----------------------------------------------------------------------------------#

# 6. Create a function, called bottles_of_beer, that accurately prints the “99 bottles of beer on the wall” song: 
# http://www.99-bottles-of-beer.net/lyrics.html. Your program should account for changes in plural vs. singular 
# nouns and should count down from 99 to 0. 
# (10 points)

def bottles_of_beer():
  '''
  Prints the lyrics of the "99 Bottles of Beer" song, counting down from 99 to 0.
  '''
   
  for i in range (99, 1, -1):
     print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
     print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
     if i == 2:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")

# bottles_of_beer()  #Time for a song eh?
      
#----------------------------------------------------------------------------------#

# 7. Evaluate the following function and revise it so that it runs without error and follows 
# Python conventions (15 points)

def checkAgeHeight(age, height):
  if type(age) != int or type(height) != int:
    print("Error: Age and height must be integers")
  elif age > 12:
     print("Old enough to ride")
     if height > 54:
        print("Tall enough to ride")
     else:
        print("Not tall enough to ride")
  elif age < 0 or height < 0:
    print("Error: Age and height must be non-negative")

  else:
     print("Not old enough to ride")
     
# checkAgeHeight(14.5, 60)  #Test non-integer age
# checkAgeHeight(14, "fifty")  #Test non-integer height       
# checkAgeHeight(14, 55)  #Test old enough and tall enough
# checkAgeHeight(11, 55)  #Test not old enough
# checkAgeHeight(14, 53)  #Test old enough but not tall enough
# checkAgeHeight(11, 53)  #Test not old enough and not tall enough
# checkAgeHeight(-5, 60)  #Test negative age
# checkAgeHeight(14, -10)  #Test negative height


#----------------------------------------------------------------------------------#

# 8. Evaluate the following function and revise it so that it runs without error and follows 
# Python conventions (15 points)

def changeNumber(myNum, myType):
  
  """
  This function will change a number from int to float or float to int
	
  Inputs:
	myNum (int/float): input number
	myType (int/float): the type we want to get back
	
	return
		myNum but with correct type
	"""

  if myType == int:
    return int(myNum)
  elif myType == float:
    return float(myNum)
  else:
    return "Error: Invalid input. Please enter an int or float for myNum, and 'int' or 'float' for myType."
  
# print(changeNumber(5.6, int))  #Test float to int
# print(changeNumber(5, float))  #Test int to float
# print(changeNumber(5, str))  #Test invalid type
# print(changeNumber("5", int))  #Test invalid number type
# print(changeNumber(5.6, "int"))  #Test invalid type input









