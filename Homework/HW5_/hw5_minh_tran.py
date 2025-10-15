'''
COMP 3005
Homework 5 - File Input/Output & Exception Handling

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



In this assignment we will be working with a Kaggle dataset 
(https://www.kaggle.com/datasets/bryan2k19/dutch-house-prices-dataset)
(https://www.kaggle.com/datasets/mirbektoktogaraev/madrid-real-estate-market). 
This is a real state dataset from the Netherlands and Madrid, Spain. The data 
contains 16 columns with 5555 entries and 58 columns with 21.7k entries respectively.
We will be working with a subset of the data split into multiple files. 

Our objective with this data is to import and analyze this data in order to help a family 
member purchace a home in the Netherlands/Madrid. They will be letting us sleep on their 
couch in exchange for this service. A fair trade.

Files associated with this HW: buyPriceMadrid.csv, buyPriceNetherlands.csv, livingSpaceMadrid.csv,
LivingSpaceNetherlands.csv, rentPriceMadrid.csv, rentPriceNetherlands.csv, extra_functions.py
'''
#--------------------------------------------------------------------------#

# 1. Create a function, called input_data, that takes a file name as an argument. 
# The function must handle an exception if the file is not found (this occurs 
# when the file does not exist, if it was misspelled or it's in a different 
# directory). The function must read in the data from the file and return it
# as a list. 
# (15 points)
def input_data(fileName):
  '''
  Reads data from a file and returns it as a list of strings
  
  Parameters:
    fileName (str): The name of the input file
  
  Returns:
    list: A list of strings, each interpreting a line from the file
  
  Errors Handled:
    FileNotFoundError: If the specified file does not exist
    TypeError: If the fileName is not a string

  '''
  dataList = list()
  try:
    if type(fileName) != str:
      raise TypeError('fileName must be a string') 
    else:
      with open(fileName, 'r',encoding='utf-8') as file:
        for line in file:
          dataList.append(line.strip())
      return dataList
  except FileNotFoundError as fnf:
    print ('File cannot be found.', fnf)


# 2. Create a function, called list_of_floats, that takes a list of values and casts
# each value to a float. The function must be able to handle exceptions dealing with
# missing values and values that cannot be cast to a float, i.e. "fdshjksd". The
# function must return a list of floats. Note: you must create an empty list inside 
# the function, and append the casted values to it, then return it. 
# (15 points)

def list_of_floats(data_list):
  '''
  Converts a list of values to a list of floats, handling exceptions for non-convertible values

  Parameters:
    data (list): A list of values to be converted to floats

  Returns:
  list: A list of floats, excluding any values that cannot be converted
  
  Errors Handled:
    ValueError: If a value cannot be converted to float, skip that thang

  '''
  float_list = list()
  for value in data_list:
    try:
      float_value = float(value)
      float_list.append(float_value)
    except ValueError as ve:
      continue # Skip values that cannot be converted to float
  return float_list


# 3. Create a function, called compute_average, that takes in a list of floats as an 
# argument. All elements in the list must be floats in order to perform any calculations.
# You cannot use any built-in function to compute the average, instead add up all the
# values and divide by the total number of values you have. Return the average (this
# should be a float). 
# (15 points)

def compute_average(float_list):
  '''
  Computes the average of a list of floats

  Parameters:
    float_list (list): A list of floats to compute the average of

  Returns:
    float: The average of the list of floats, or a message if there is no value to compute
  '''

  if len(float_list) == 0:
    return 'No data to compute average'
  total = 0.0 #for sum of values
  count = 0 #for total number of values
  for value in float_list:
    total += value
    count += 1
  average = total / count
  return average

# 4. Create a function, called filtered_data, that takes filename and max_price as arguments,
# of types list and float respectively. The function should loop over the list and store the
# results that satisfy the max_price criteria in a new list (amount is <= max_price).
# (In your loop use : 
# filtered_results = []
# filtered_results.append(filtered_data_point)). 
# Return the list with the new results. The function must handle the exception of getting an 
# incorrect max value, i.e. "bjfdsk". (15 points)

def filtered_data(data_list, max_price):
  '''
  Filters a list of floats based on a maximum price

  Parameters:
    data_list (list): A list of floats to be filtered
    max_price (float): The maximum price threshold for filtering

  Returns:
    list: A list of floats that are less than or equal to the max_price threshold

  Errors Handled:
    TypeError: If max_price is not a float, return an empty list
  '''
  filtered_results = []

  try:
    if type(max_price) != float:
      raise TypeError('max_price must be a float') # Raise TypeError if max_price is not a float
    
    for data_point in data_list:
      if data_point <= max_price:
        filtered_results.append(data_point)

    return filtered_results
  
  except TypeError as te:
    print('max_price must be a float.', te)


# 5. Create a function, called real_state_analysis, that takes a location, type string. The 
# function must ask the user for the file names for buy prices, living space and rent prices 
# while handling the file not found error. 

# The function must ask the user to enter a file name until they entered a valid file name.
# Note: the file names must have the extension .csv to work

# The function must then compute the average buy price, average rent price and average living 
# space. Perform checks on your data as the data may not be very clean (you should expect 
# missing values and negative values. You must deal with them).

# Write the results in a file called : real_state_analysis.csv using the following format :
# location, avg_buy_price, avg_rent_price, avg_sqft

# Note 1: the living space is in square meters, rent and buy prices are in euros, so create
# a second file, helper_functions.py and use our previously defined function to convert sqmt 
# to sqft and euros to dollars (you may need to modify the function to make it work).
# Note 2: You must also use whichever functions created in this homework to accomplish this task.
# Note 3: You will need to call the function twice, once for the data for Madrid and another for
# the Netherlands
# The output for the function should look like this :
# Madrid, 578091.9661429492, 1434.4682101167316, 883.9385353229587
# Netherlands, 602963.3547672321, 3014.7843377841937, 1576.2050598919893
# (40 points)

def real_state_analysis(location):
  import extra_functions as ef #alias for shorter code
  buy_file_name = ''
  rent_file_name = ''
  space_file_name = ''
  
  while True:

    try:
      buy_file_name = input(f'Enter the buy price file name for {location} (with .csv extension): ') # ask for file name
      buy_data = input_data(buy_file_name) #read data from file

      if not buy_data: # if there is no data, meaning file not found, meaing no data was returned from input_data function
        raise FileNotFoundError #raise error if file not found
      break #exit loop if file is found

    except FileNotFoundError:
      print('File not found. Please try again.')

  while True:

    try:
      rent_file_name = input(f'Enter the rent price file name for {location} (with .csv extension): ')
      rent_data = input_data(rent_file_name)

      if not rent_data:
        raise FileNotFoundError
      break

    except FileNotFoundError:
      print('File not found. Please try again.')

  while True:

    try:
      space_file_name = input(f'Enter the living space file name for {location} (with .csv extension): ')
      space_data = input_data(space_file_name)

      if not space_data:
        raise FileNotFoundError
      break

    except FileNotFoundError:
      print('File not found. Please try again.')

  buy_floats = list_of_floats(buy_data) # Convert data to floats lists
  rent_floats = list_of_floats(rent_data) 
  space_floats = list_of_floats(space_data) 

# Remove negative values
  # for price in buy_floats: 
  #   if price > 0:
  #     continue
  #   else:
  #     buy_floats.remove(price) 

  # for price in rent_floats:
  #   if price > 0:
  #     continue
  #   else:
  #     rent_floats.remove(price)

  # for space in space_floats:
  #   if space > 0:
  #     continue
  #   else:
  #     space_floats.remove(space)

  #using list comprehensions (new method)
  buy_floats = [price for price in buy_floats if price > 0]
  rent_floats = [price for price in rent_floats if price > 0]
  space_floats = [space for space in space_floats if space > 0]

  avg_buy_price_eur = compute_average(buy_floats) # Compute averages
  avg_rent_price_eur = compute_average(rent_floats)
  avg_space_sqm = compute_average(space_floats)

  eu_to_us = ef.europe_us(avg_space_sqm, avg_buy_price_eur, avg_rent_price_eur) # Convert to USD and sqft

  avg_buy_price_usd = eu_to_us[1] #indexing because function from extra_functions.py returns a tuple
  avg_rent_price_usd = eu_to_us[2]
  avg_living_space_sqft = eu_to_us[0]


  with open('real_state_analysis.csv', 'w', encoding='utf-8') as file:
    file.write('location, avg_buy_price, avg_rent_price, avg_sqft\n')
    file.write(f'{location}, {avg_buy_price_usd}, {avg_rent_price_usd}, {avg_living_space_sqft}\n')
  return (location, avg_buy_price_usd, avg_rent_price_usd, avg_living_space_sqft)


#-------------------------- TESTS ------------------------#



if __name__ == '__main__':
  
  #Test 1
  # print(input_data('buyPriceMadrid.csv'))

  #Test 2
  # print(list_of_floats(input_data('buyPriceMadrid.csv')))

  #Test 3
  # print(compute_average(list_of_floats(input_data('buyPriceMadrid.csv'))))

  #Test 4
  # print(filtered_data(list_of_floats(input_data('buyPriceMadrid.csv')), 300000.0))

  #Test 5
  # print(real_state_analysis('Madrid'))

    # buyPriceMadrid.csv
    # rentPriceMadrid.csv
    # livingSpaceMadrid.csv

  # print(real_state_analysis('Netherlands'))

    # buyPriceNetherlands.csv
    # rentPriceNetherlands.csv
    # livingSpaceNetherlands.csv