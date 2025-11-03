"""
COMP 3005
Homework 8 - Dictionaries & JSON Files

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


# Table with type equivalence between JSON and Python
# Python	            JSON
#--------------------------------
# dict	                object
# list, tuple	        array
# str	                string
# int, long, float	    number
# True	                true
# False	                false
# None	                null

"""

###----------------------###
###-----Dictionaries-----###
###----------------------###

# 1. Write a function, called list_to_dict, that takes a list as an argument
# and returns a dictionary containing the keys 1 through n, where n is the
# size of the list, and the values correspond to the values in the list.
# For example, if the list is [2, 6, 6, 1, 7, 9] then the dictionary maps:
# 1 —> 2, 2 —> 6, 3 —>6, 4 —> 1, 5 —> 7 and 6 —> 9.
# In Python this would be: {1:2, 2:6, 3:6, 4:1, 5:7, 6:9}
# (20 points)

def list_to_dict(lst):
  '''
  Turns a list into a dictionary with keys being 1 to n, with n being the size of the list, and the values paired
  with the keys corresponding to the values in the list provided

  Parameters:
    lst: a list of values

  Returns:
    dictionary: a dictionary with keys being 1 to n, with n being the size of the list, and the values paired
    with the keys corresponding to the values in the list    
  # '''
  
  # edge cases
  if type(lst) is not list:
    raise TypeError('Input must be a list.')
  if lst == []:
    raise ValueError('Input cannot be empty.')

  # for i+1 starts at 1, paired with lst[i] in range the list's length
  return {i+1 : lst[i] for i in range(len(lst))}


# 2. Write a function, called new_dict, that takes a dictionary as an argument
# and returns a new dictionary with the keys and values inverted (keys become
# values and values become keys).
# What happens if there are duplicate values?
# (10 points)

def new_dict(dict_input):
  '''
  Returns a new dictionary with the keys and values inverted (keys:values --> values:keys)

  Parameters:
    dictionary: a dictionary

  Returns:
    a new dictionary: a new dictionary with keys:values pair inverted
  '''

  # edge cases
  if type(dict_input) is not dict:
    raise TypeError('Input must be a dictionary.')
  if dict_input == {}:
    raise ValueError('Input cannnot be empty.')

  dict_keys = list(dict_input.keys())
  dict_values = list(dict_input.values())

  return {dict_values[i] : dict_keys[i] for i in range(len(dict_input))}



# 3. Write a function, called unique_elems, that takes a list of values as a
# parameter and determines if all elements are unique (no repeated values).
# Return True if all values are unique, False otherwise. Think of a way to use
# dictionary to perform this task.
# (10 points)

def unique_elems(list_of_vals):
  '''
  Determines if a list of values only contains unique values

  Parameters:
    list_of_vals: a list of values

  Returns:
    boolean: True if a list_of_vals only contains unique values, False otherwise 
  '''

  # edge cases
  if type(list_of_vals) is not list:
    raise TypeError('Input must be a list.')
  if list_of_vals == []:
    raise ValueError('Input cannot be empty.')

  # keys : values pairs as item : count
  new_dict = {list_of_vals[i] : i+1 for i in range(len(list_of_vals))}

  # if there's a duplicate, dict updates it => keys can only be unique values, hence compare their lengths
  if len(list_of_vals) != len(new_dict):
    return False
  return True

# 4. Write a function, called val_frequency, that given a list of values as a
# parameter, counts the frequencies for each value in the list. You can do this
# by returning a dictionary (think about what the key should be and what value
# should be associated with it).
# For example, if the list is [1, 3, 5, 2, 1, 2, 5, 8, 4, 5] then we have:
# 2 x 1's, 1 x 3's, 3 x 5's, 2 x 2's, 1 x 4's, 1 x 8’s
# In Python this would be: {1: 2, 3: 1, 5: 3, 2: 2, 8: 1, 4: 1}
# (10 points)

# slower run time
# def val_frequency(list_of_vals):
  # '''
  # Counts the times a value is repeated and return a dictionary with keys being the value and 
  # values being the count of said value being repeated

  # Parameters:
  #   list_of_vals: a list of values

  # Returns:
  #   dictionary: list values as keys & counts of value repetition as values
  # '''

  # if type(list_of_vals) is not list:
  #   return 'Input must be a list.'
  # if list_of_vals == []:
  #   return 'Input cannot be empty.'

  # n = len(list_of_vals)
  # dup_items = []
  # new_dict = {}

  # for x in range(n): # for every x in list
  #   for y in range(n): # compare with very y in list
  #     if list_of_vals[x] == list_of_vals[y]: # if there are duplicates
  #       dup_items.append(x) # add it to dup_items
  #     new_dict[list_of_vals[x]] = len(dup_items) # all added, exit 'if', add to dict {x:length of dup_items}
  #   dup_items = [] # reset dup_item after every x in list is compared to every item in list 
  # return new_dict # and abracadabra 

def val_frequency(list_of_vals):
  '''
  Counts the times a value is repeated and return a dictionary with keys being the value and 
  values being the count of said value being repeated

  Parameters:
    list_of_vals: a list of values

  Returns:
    dictionary: list values as keys & counts of value repetition as values
  '''

  # edge cases
  if type(list_of_vals) is not list:
    raise TypeError('Input must be a list.')
  if list_of_vals == []:
    raise ValueError('Input cannot be empty.') 

  new_dict = {}
    
  # Iterate through the list only once
  for item in list_of_vals:
      # If the item is already a key, increment its count
      if item in new_dict:
          new_dict[item] += 1
      # If it's a new item, initialize its count to 1
      else:
          new_dict[item] = 1
          
  return new_dict


# 5. Write a function, called adds_to_K, that given an integer k and a list of n
# unordered integers A, determines if there is a pair of distinct integers in A
# that add up to k. Returns True if there are, False otherwise.
# For example : given [1, 6, 7, 3, 7, 10, 3] if k=13 then there is a pair of
# integers that add up to 13 : 10 and 3. If k=14 then there isn’t a pair of distinct
# integers that add up to 14 (can’t use 7 twice even if it appears twice in the list)
# (10 points)

def adds_to_K(k, list_of_vals):
  '''
  Determines if a pair of distinct values in list_of_vals adds up to k

  Parameters:
    k: an integer
    list_of_vals: a list of values

  Returns:
    boolean: True of there is a pair of dinstinct values that adds up to k, False otherwise
  '''

  # edge cases
  if type(k) is not int:
    raise TypeError('k must be an integer.')
  if type(list_of_vals) is not list:
    raise TypeError('list_of_vals must be a list.')
  if list_of_vals == []:
    raise ValueError('list_of_vals cannot be empty.')

  new_dict = {}

  for i in list_of_vals: # use dictionary to keep only distinct values as keys
    if i in new_dict: 
      new_dict[i] += 1
    else:
      new_dict[i] = 1

  dict_keys = list(new_dict.keys())
  print(dict_keys)

  for x in dict_keys:
    for y in dict_keys:
      if x + y == k:
        return True
    return False

###-------------------###
###-----JSON FIle-----###
###-------------------###
import json


# 6. Write a function, called senators_info, that takes a filename (senators.json)
# as an argument. It should load the json file and extract the Senator's
# following information:
# First name
# Last name
# State
# Party
# Start date (since when they've been Senators)
# Congress number (which sessions of Congress they were Senators for)
# Contact form
# Phone number
# Twitter handle
# Birthday
# Nickname
# The function should write the senators information to a json file
# called senatorsInfo.json. Use an indent of 2 to make the data more
# readable. The function should also return the data, this should
# be a list of dictionaries.
# Hint: You may want to use the get() method when getting the data
# (20 points)

def senators_info(filename):
  '''
  Returns a dictionary with keys as follow:
  # First name
  # Last name
  # State
  # Party
  # Start date (since when they've been Senators)
  # Congress number (which sessions of Congress they were Senators for)
  # Contact form
  # Phone number
  # Twitter handle
  # Birthday
  # Nickname
  and values as the extracted information from the file

  Parameters:
    filename: file whose information to be extracted as a string

  Returns:
    json: a json file with extracted information
    list: a list of dictionaries with extracted information 
  '''
  try:

    with open(filename, 'r') as f:
      data = json.load(f)

    senators_list = []

    for senator in data['objects']:
      senator_dict = {
        'first_name': senator.get('person').get('firstname'),
        'last_name': senator.get('person').get('lastname'),
        'state': senator.get('state'),
        'party': senator.get('party'),
        'start_date': senator.get('startdate'),  # Assuming 'senator_rank' indicates start date
        'congress_numbers': senator.get('congress_numbers'),
        'contact_form': senator.get('extra').get('contact_form'),
        'phone_number': senator.get('phone'),
        'twitter_handle': senator.get('person').get('twitterid'),
        'birthday': senator.get('person').get('birthday'),
        'nickname': senator.get('person').get('nickname')
      }
      senators_list.append(senator_dict)

    with open('senatorsInfo.json', 'w') as f:
      json.dump(senators_list, f, indent=2)
    return senators_list
  
  except FileNotFoundError:
    raise FileNotFoundError(f"The file {filename} was not found.")

# 7. Write a function, called no_contact_form, that takes in a filename,
# loads the data in from a json file and returns a list containing the first
# and last name of the senators that do
# not have a contact form.
# (15 points)

def no_contact_form(filename):
  '''
  Returns a list of senators without a contact form

  Parameters:
    filename: file whose information to be extracted as a string

  Returns:
    list: a list of senators without a contact form
  '''
  try: 
    
    with open(filename, 'r') as f:
      data = json.load(f)

    no_contact_list = []

    for senator in data['objects']:
      if not senator.get('extra').get('contact_form'):
        full_name = f"{senator.get('person').get('firstname')} {senator.get('person').get('lastname')}"
        no_contact_list.append(full_name)

    return no_contact_list

  except FileNotFoundError:
    raise FileNotFoundError(f"The file {filename} was not found.")

# 8. Write a function, called congress_session_members, that takes a congress session session_number (int) 
# and a filename (str). It should load the data created in question 6 and search for all the senators that 
# were part of that particular session of congress. The function should write the resulting senators to a 
# file called congress_session{session_number}.json and returns a list of every senator that was part of t
# he Senate for the given session_number. It should return an empty list if none of the senators were members 
# for that congress. 

# (Congress session 1 should have nobody in it (except maybe Chuck Grassley
# and Mitch McConnell)).
# The numbers of senators for each Congress session available.
# sessionNumber 116 = 33
# sessionNumber 117 = 64
# sessionNumber 118 = 100
# sessionNumber 119 = 66
# sessionNumber 120 = 34
# all other session numbers should be empty
# (15 points)

def congress_session_members(session_number, filename):
  '''
  Returns a list of senators that were part of a particular session of congress

  Parameters:
    session_number: an integer representing the congress session number
    filename: file whose information to be extracted as a string

  Returns:
    list: a list of senators that were part of a particular session of congress
  '''

  try:

    with open(filename, 'r') as f:
      data = json.load(f)

    session_senators = []
    count = 0

    for senator in data:
      if session_number in senator.get('congress_numbers', []):
        session_senators.append(senator)
        count += 1
    # session_senators.append(f'Total senators in session {session_number}: {count}')

    output_filename = f'congress_session{session_number}.json'
    with open(output_filename, 'w') as f:
      json.dump(session_senators, f, indent=2)

    return session_senators
  except FileNotFoundError:
    raise FileNotFoundError(f"The file {filename} was not found.")

#-----------------------------------------------------------------------------------------------

if __name__ == '__main__':
  pass

# test 1
# print(list_to_dict('string'))
# print(list_to_dict([]))
# print(list_to_dict(['dog','cat','duck']))
# print(list_to_dict([2, 6, 6, 1, 7, 9]))

# test 2
# print(new_dict([1,2,3]))
# print(new_dict({}))
# print(new_dict({'first_name': 'john', 'last_name': 'wick', 'occupation':'ethical hitman'}))
# print(new_dict({'count': 90}))

# test 3
# print(unique_elems(3000))
# print(unique_elems([]))
# print(unique_elems(['edmuntosaurus', 'quetzalcoatlus', 'troodon', 'edmuntosaurus']))
# print(unique_elems(['edmuntosaurus', 'quetzalcoatlus', 'troodon']))

# test 4 
# print(val_frequency((2,4)))
# print(val_frequency([])) 
# print(val_frequency(['dog','cat','buffalo','wombat','wombat','dog','buffalo','dog']))
# print(val_frequency([1, 3, 5, 2, 1, 2, 5, 8, 4, 5]))
# print(val_frequency(['lion','wolf','stag','dragon']))

# test 5
# print(adds_to_K('ten', [6,5,4]))
# print(adds_to_K(10, (7,3,2)))
# print(adds_to_K(10, []))
# print(adds_to_K(10, [7,4,5,3,5]))
# print(adds_to_K(10, [1,2,5,6,0]))

# test 6
# print(senators_info('demo.json'))
# print(senators_info('senators.json'))

# test 7
# print(no_contact_form('demo.json'))
# print(no_contact_form('senators.json'))

# test 8
# print(congress_session_members(115, 'demo.json'))
# print(congress_session_members(116, 'senatorsInfo.json'))
# print(congress_session_members(117, 'senatorsInfo.json'))
# print(congress_session_members(118, 'senatorsInfo.json'))
# print(congress_session_members(119, 'senatorsInfo.json'))
# print(congress_session_members(120, 'senatorsInfo.json'))
# print(congress_session_members(1, 'senatorsInfo.json'))
