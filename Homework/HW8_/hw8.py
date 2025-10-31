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


# 2. Write a function, called new_dict, that takes a dictionary as an argument
# and returns a new dictionary with the keys and values inverted (keys become
# values and values become keys).
# What happens if there are duplicate values?
# (10 points)


# 3. Write a function, called unique_elems, that takes a list of values as a
# parameter and determines if all elements are unique (no repeated values).
# Return True if all values are unique, False otherwise. Think of a way to use
# dictionary to perform this task.
# (10 points)


# 4. Write a function, called val_frequency, that given a list of values as a
# parameter, counts the frequencies for each value in the list. You can do this
# by returning a dictionary (think about what the key should be and what value
# should be associated with it).
# For example, if the list is [1, 3, 5, 2, 1, 2, 5, 8, 4, 5] then we have:
# 2 x 1's, 1 x 3's, 3 x 5's, 2 x 2's, 1 x 4's, 1 x 8’s
# In Python this would be: {1: 2, 3: 1, 5: 3, 2: 2, 8: 1, 4: 1}
# (10 points)


# 5. Write a function, called adds_to_K, that given an integer k and a list of n
# unordered integers A, determines if there is a pair of distinct integers in A
# that add up to k. Returns True if there are, False otherwise.
# For example : given [1, 6, 7, 3, 7, 10, 3] if k=13 then there is a pair of
# integers that add up to 13 : 10 and 3. If k=14 then there isn’t a pair of distinct
# integers that add up to 14 (can’t use 7 twice even if it appears twice in the list)
# (10 points)

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


# 7. Write a function, called no_contact_form, that takes in a filename,
# loads the data in from a json file and returns a list containing the first
# and last name of the senators that do
# not have a contact form.
# (15 points)


# session_number (int) and a filename (str). It should load the data created in question 6
# and search for all the senators that were part of that particular session of congress.
# The function should write the resulting senators to a file called
# congress_session{session_number}.json and returns a list of every senator that was
# part of the Senate for the given session_number. It should return an empty
# list if none of the senators were members for that congress.
# (Congress session 1 should have nobody in it (except maybe Chuck Grassley
# and Mitch McConnell)).
# The numbers of senators for each Congress session available.
# session_number 116 = 33
# session_number 117 = 64
# session_number 118 = 100
# session_number 119 = 66
# session_number 120 = 34
# all other session numbers should be empty
# (15 points)
