'''
COMP 3005
Homework 9 - Recursion

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

# You are not allowed to use iteration to solve any of the problems below.

# 1. Write a recursive function, called recFactorial, that takes an integer x as argument and
# returns the x! (x factorial). (10 points)
# For example : 5! = 5*4*3*2*1

def recFactorial(x):
  '''
  Returns the factorial of the input number

  Parameters:
    x: an integer

  Rerturns:
    integer: factorial of x: x!
  '''

  # base case
  if x == 1:
    return 1
  # keep multiplying x with x-1 till it reaches 1
  else:
    return x * recFactorial(x-1)


# 2. Write a recursive function, called dogLegs, that takes number of dogs as argument and
# returns the number of dog legs (assume each dog has 4 legs). (20 points)

def dogLegs(num_of_dogs):
  '''
  Calculates the number of legs in total given the number of dogs

  Parameters:
    num_of_dog: integer, the number of dogs whose legs in total to be calculated

  Returns:
    integer: the number of dog legs
  '''

  # base case
  if num_of_dogs == 1:
    return 4
  # keep adding 4 legs to num_of_dogs till it reaches 1 dog
  else:
    return 4 + dogLegs(num_of_dogs-1)


# 3. A triangle is made of blocks and each row has one more block than the one below it so the
# first row from the top has 1 block, then 2 blocks below that, then 3 blocks below that…etc.
# Write a recursive function, called numBlocks, that counts the number of blocks in a
# triangle of height h and returns it. (15 points)

def numBlocks(h):
  '''
  Retuns the number of blocks in a triangle of height h

  Parameters:
    h: height of a triangle

  Returns:
    integer: the number of blocks in a triangle of height h
  '''

  # base case
  if h == 1:
    return 1
  # keep adding h to numblock(h-1) till it reaches height = 1
  # since the number of blocks at base = height always (height = 4, # of blocks at base = 4)
  else:
    return h + numBlocks(h-1)


# 4. Write a recursive function, called containsTarget, that takes a list and a target value and
# returns true if the list contains the target value or false otherwise. (10 points)

def containsTarget(List, target):
  '''
  Returns True if list L contains target value, False otherwise

  Parameters:
    List: list of values
    target: value whose inclusion in list L needs determining

  Returns:
    boolean: True if list L contains target value, False otherwise
  '''

  n = len(List)

  # base cases: empty list = False | first element is target = True
  if n == 0:
    return False
  if List[0] == target:
    return True
  # else slice the first element off and keep comparing
  else:
    return containsTarget(List[1:], target)


# 5. Write a recursive function, called countTarget, that takes a list of values and a target value
# and returns the number of times target appears in list. For example if the target is 4 and the
# list is [1, 3, 5, 4, 2, 4] then the function returns 2. (15 points)

def countTarget(List, target):
  '''
  Counts the number of times a target appears in the list of values

  Parameters:
    List: a list of values
    target: target to be counted

  Returns:
    integer: the count of occurence of the target value in the list
  '''

  # base cases: empty list = 0, finds target = 1 + the rest
  if len(List) == 0:
    return 0
  if List[0] == target:
    return 1 + countTarget(List[1:], target)
  # else keep comparing the rest
  else:
    return countTarget(List[1:], target)


#6. Write a recursive function, called countZZ, that takes a string as an argument and
# computes the number of times lowercase "ZZ" appears in the string. (10 points)
# For example "hellozz Worzzld" would return 2 and “hellozzz Worzzzld” would also return 2.

def countZZ(string):
  '''
  Counts the times "zz" appears in the string

  Parameters:
    string: a string

  Returns:
    integer: the number of occurences of "zz" in a string
  '''

  # base cases: less than 2 letters in string = 0, string starts with 'zz' => 1 + countZZ(slice off first 2)
  if len(string) < 2:
    return 0
  if string.startswith('zz'):
    return 1 + countZZ(string[2:])
  # if not, slice off the first one
  else:
    return countZZ(string[1:])


# 7. Write a recursive function, elimDuplicates, that takes a string as an argument and returns a
# new string with all adjacent duplicate characters (a character followed by the same character) removed. (20 points)
# For example "hello" will become "helo" and "wohooo" will become "woho"

def elimDuplicates(string):
  '''
  Returns a new string with adjacent duplicate characters eliminated

  Parameters:
    string: a string to be scrutinized

  Returns:
    string: a new string with adjacent duplicate characters emliminated
  '''
  # base cases: less than 2 letters in string -> return that string
  #             if the 2 adjacent string are the same -> slice off the first letter
  if len(string) < 2:
    return string
  if string[0] == string[1]:
    return elimDuplicates(string[1:])
  # if not, add that string back to the first-sliced string
  else:
    return string[0] + elimDuplicates(string[1:])


#--------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
  pass

# test 1
  # print(recFactorial(5))

# test 2
  # print(dogLegs(10))

# test 3
# print(numBlocks(3))

# test 4
# print(containsTarget(['cat', -98, True, 'dog', 1, 2], 'dog'))  
# print(containsTarget(['cat', -98, False, 'dog', 1, 2], 'dawg'))  

# test 5
# print(countTarget(['bowl', 'spoon', 'bowl', 'fork', 'bowl'], 'bowl'))
# print(countTarget([1, 3, 5, 4, 2, 4], 4))

# test 6
# print(countZZ('hellozz Worzzld'))
# print(countZZ('hellozzz Worzzzld'))

# test 7
# print(elimDuplicates('success'))
# print(elimDuplicates('hello'))
# print(elimDuplicates('woohoo'))
