'''
COMP 3005
Homework 6 - Lists & Tuples

General Homework Guidelines: 
- Do not use built-in functions
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

# In this assignment we will be working with a real estate dataset (hw6_data.csv) from the Netherlands. 
# The data contains 4 columns and 5556 entries. 
# Our objective with this data is to import and analyze this data in order to help a family member purchace 
# a home in the Netherlands. 



###---------------###
###-----Lists-----###
###---------------###


# 1. Create a function, called import_data, that takes a filename as an argument. 
# The function must handle an exception when the file is not found (this occurs when the file does not exist, 
# if it was misspelled or it's in a different directory). 
# If the exception is raised, the function must ask the user to re-enter the file name and check again. 
# Repeat this as many times as needed until the data is read in. If the user enters nothing, the function should 
# terminate. The function should return the data that was read in, it should be of type list, or return an empty 
# list if the user terminated the function. The output list should have length 5556 (15 points)

def import_data(filename):
  '''
  Imports data from a specified file, handling file not found exceptions

  Parameters:
    filename (str): The name of the file

  Returns:
    list: A list containing the data read from the file, or an empty list if the user terminates
  '''
  data = []  # Initialize an empty list to store the data
  while True:
      try:
          with open(filename, 'r') as file:  # Attempt to open the file
              data = file.readlines()  # Read all lines from the file
          break  # Exit the loop if the file is successfully read
      except FileNotFoundError:  # Handle the case where the file is not found
          filename = input("File not found. Please re-enter the file name (or press Enter to exit): ")
          if filename == "":  # Check if the user wants to terminate
              return []  # Return an empty list if terminated
  return data  # Return the list of data read from the file

# 2. Create a function, called cast_data, that takes in the data read in by the previous function, 
# this should be a list of strings. The function should perform the following casts : 
    
# Price --> float
# Lot size (m2) --> float
# Living space size (m2) --> float
# Build year --> int

# The function should return two objects: a list of lists (each complete row of data is a separate list) as well as 
# the number of rows that have been excluded as bad data. The list output should be of the form :

# [
# ...
# [859000,5440,300,2017],
# [389000,290,108,1973],
# [399000,219,129,1976],
# ...
# ]

# You should only append rows that have values for all columns :
# 859000,5440,300,2017      #this row should be included
# 389000,290,108,1973       #this row should be included
# 349000,281,80,            #this row should not be included, it doesn't have a value for the year column
# 399000,219,129,1976       #this row should be included

# Be mindful of errors in the data, you will need to handle exceptions !
# Output list should have length 5438. (15 points)

def cast_data(data):
  '''
  casts data from strings to appropriate types and filters out incomplete rows

  Parameters:
    data (list of str): The list of strings representing the data

  Returns:
    tuple: A tuple containing a list of lists with casted data and the number of excluded rows
  '''

  casted_data = []  # List to store the casted data
  excluded_count = 0  # Counter for excluded rows

  for line in data:
      values = line.strip().split(',')  # Split the line into values
      if len(values) != 4:  # Check if the row has all four columns
          excluded_count += 1  # Increment excluded count
          continue  # Skip to the next iteration

      try:
          price = float(values[0])  # Cast price to float
          lot_size = float(values[1])  # Cast lot size to float
          living_space = float(values[2])  # Cast living space to float
          build_year = int(values[3])  # Cast build year to int

          casted_data.append([price, lot_size, living_space, build_year])  # Append the casted row to the list
      except ValueError:  # Handle casting errors
          excluded_count += 1  # Increment excluded count
          continue  # Skip to the next iteration
  return casted_data, excluded_count  # Return the casted data and excluded count

# 3. Create a function, called average_values, that takes in a list of lists (output from question 2). 
# The list contains the price, lot size, living space and build year. 
# The function must deal with potential missing values (a back up check), keeping track of the number of 
# data points collected for each field (required for computing the average), and realistic data points for 
# the "year" column (say any positive number up to and including 2023). 
# The function should return a tuple containing the average home price, lot size, living space, and build year 
# for all homes. 
# Your output should be (557707.7581831556, 686.6248620816476, 146.34608311879367, 1968.9804836656767) (15 points)

def average_values(data):
  '''
  Calculates the average values for price, lot size, living space, and build year

  Parameters:
    data (list of lists): The list of lists containing real estate information

  Returns:
    tuple: A tuple containing the average price, lot size, living space, and build year
  '''

  total_price = 0.0 # Variable to accumulate total price
  total_lot_size = 0.0 # Variable to accumulate total lot size
  total_living_space = 0.0 # Variable to accumulate total living space
  total_build_year = 0 # Variable to accumulate total build year

  count_price = 0 # Counter for valid price entries
  count_lot_size = 0 # Counter for valid lot size entries
  count_living_space = 0 # Counter for valid living space entries
  count_build_year = 0 # Counter for valid build year entries

  for row in data:
    price, lot_size, living_space, build_year = row  # Unpack the row

    # Total price and total count for prices
    if isinstance(price, float):
        total_price += price
        count_price += 1

    # Total lot size and total count for lot sizes
    if isinstance(lot_size, float):
        total_lot_size += lot_size
        count_lot_size += 1

    # Total living space and total count for living spaces
    if isinstance(living_space, float):
        total_living_space += living_space
        count_living_space += 1

    # Total build year and total count for build years, positive and <= 2023
    if isinstance(build_year, int) and 0 < build_year <= 2023:
        total_build_year += build_year
        count_build_year += 1

  # Calculate averages
  avg_price = total_price / count_price if count_price > 0 else 0
  avg_lot_size = total_lot_size / count_lot_size if count_lot_size > 0 else 0
  avg_living_space = total_living_space / count_living_space if count_living_space > 0 else 0
  avg_build_year = total_build_year / count_build_year if count_build_year > 0 else 0

  return (avg_price, avg_lot_size, avg_living_space, avg_build_year)  # Return the averages as a tuple

# 4. Create a function called filter_by_values that takes in a list containing real estate information, 
# a minimum price and maximum price, these must be of type list, float and float respectively. 
# The function should return the average home price, lot size, living space, and build year of all homes 
# that fit between the minimum and maximum home values given. Result should be returned as a tuple in the 
# order price, lot size, living space, and build year. 
# When function called with min_price = 100000 and max_price = 400000, 
# output should be:(324395.9323770492, 216.56045081967213, 110.17930327868852, 1966.869722557298) (15 points)

def filter_by_values(data, min_price, max_price):
  '''
  
  Filters real estate data by price range and calculates average values
  
  Parameters:
    data (list of lists): The list of lists containing real estate information
    min_price (float): The minimum price for filtering
    max_price (float): The maximum price for filtering

  Returns:
    tuple: A tuple containing the average price, lot size, living space, and build year for filtered homes
  '''

  filtered_data = []  # List to store filtered data
  for row in data:
      price = row[0]  # Extract the price from the row, row[0] corresponds to price
      if min_price < price and price < max_price:  # Check if the price is within the specified range
          filtered_data.append(row)  # Add the row to the filtered data list
  return average_values(filtered_data)  # Return the average values of the filtered data

###----------------###
###-----Tuples-----###
###----------------###


# 5. Write a function, called min_max_tuple, that takes a list of numbers and returns the smallest element and 
# the largest element as a tuple (smallest, largest). Cannot use the built-in functions min()/max(). 
# You may use Python's math module if you think it will be helpful - hint, take a look at the fixed value constants
# that are available . For example : lst = [6, 3, 8, 23, -4, 35] should return (-4, 35) (15 points)

import math
def min_max_tuple(numbers):
  '''
  Finds the minimum and maximum values in a list of numbers

  Parameters:
    numbers (list of float): The list of numbers to evaluate

  Returns:
    tuple: A tuple containing the minimum and maximum values
  '''

  if not numbers:  # Check if the list is empty
      return (None, None)  # Return None for both min and max if the list is empty
  
  min_value = math.inf  # Initialize min_value to positive infinity
  max_value = -math.inf  # Initialize max_value to negative infinity

  for num in numbers:  # Iterate through each number in the list
    if num < min_value:  # Check if the current number is less than the current min_value
        min_value = num  # Update min_value
    if num > max_value:  # Check if the current number is greater than the current max_value
        max_value = num  # Update max_value
  return (min_value, max_value)  # Return the min and max as a tuple

# 6. Write a function, called all_pairs, that takes two lists as paramters, x and y, and returns a new list 
# containing all possible pairs consisting of one element from x and one element from y as long as they are 
# not the same element. Cannot use built-in functions or sets. 
# For example: If the list x = [1, 4, 6, 8] and y = [5, 2, 6] 
# then the result is the list [(1, 5), (1, 2), (1, 6), (4, 5), (4, 2), (4, 6), (6, 5), 
# (6, 2), (8, 5), (8, 2), (8, 6)]. Note that (6, 6) doesn't appear because they are the same element. (15 points)

def all_pairs(x, y):
  '''
  Generates all possible pairs from two lists, excluding pairs with identical elements

  Parameters:
    x (list): The first list of elements
    y (list): The second list of elements

  Returns:
    list of tuples: A list containing all valid pairs as tuples
  '''
  pairs = []

  for element_x in x:  # Iterate through each element in list x
    for element_y in y:  # Iterate through each element in list y
        if element_x != element_y:  # Check if the elements are not the same
            pairs.append((element_x, element_y))  # Append the pair as a tuple to the pairs list
  return pairs  # Return the list of pairs

# 7. Write a function, called remove_dups, that takes a list of tuples and removes any duplicate tuples and 
# returns the modified list. Cannot use built-in functions nor sets. 
# For example if the list contains [(1, 2), (1, 4, 5), (1, 2), (3, 5)] 
# then the list will become [(1, 2), (1, 4, 5), (3, 5)]. (10 points)

def remove_dups(tuples_list):
    '''
    Removes duplicate tuples from a list of tuples

    Parameters:
    tuples_list (list of tuples): The list of tuples from which to remove duplicates

    Returns:
    list of tuples: A new list containing only unique tuples
    '''
    unique_tuples = []  # List to store unique tuples
    for tup in tuples_list:
        if tup not in unique_tuples:  # Check if the tuple is already in the unique list with "not in"
            unique_tuples.append(tup)  # Add it if it's not a duplicate
    return unique_tuples  # Return the list of unique tuples

#--------------------------------------------------------------------------#
if __name__ == '__main__':
    pass
    # You can use this area to test your functions as you write them.
    # However, please comment out all tests before submission.


# test1
#print(import_data("hw6_data.csv"))

# test2
# print(cast_data(import_data("hw6_data.csv")))

# test3
# print(average_values(cast_data(import_data("hw6_data.csv"))[0])) #row[0] to get the list of lists only

# test4
# print(filter_by_values(cast_data(import_data("hw6_data.csv"))[0], 100000, 400000)) #row[0] to get the list of lists only

# test5
# print(min_max_tuple([6, 3, 8, 23, -4, 35]))

# test6
# print(all_pairs([1, 4, 6, 8], [5, 2, 6]))

# test7
# print(remove_dups( [(1, 2), (1, 4, 5), (1, 2), (3, 5)] ))