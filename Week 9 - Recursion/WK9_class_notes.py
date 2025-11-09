#### Recursion ####

print(f'\n\n ### Recursion ###')

'''
Recursive functions are functions that repeatedly calls itself until some condition is met. They are of value when a
complex problem can be broken down into repeating subproblems. In other words a problem that can be broken down into
smaller versions of itself.

if a problem can be broken down into similar subproblems which can be solved individually, and whose solutions can be combined together to get the overall solution

Recursive functions consist of:

1) base case - a stopping condition (smallest
instance of the same problem). We provide an explicit answer for the base case.

2) a recursive case - that calls to itself.

For the recursive function, we generalize the pattern and then add it to the base case to find our solution.

Allows data processing in multiple steps.
Similar to iterating(e.g., while loop) with a condition
A 'base case' serves to stop a recursive process

Recursion lends itself to hierarchical data structures: e.g., unnest data/arrays in data tables and 'stacking' values into single col.
We might not know how much unnesting is required. e.g., tables within tables, json files

An example of a API query and Json return -> https://jsonapi.org/examples/

	Recursion 										Iteration

	Stops when base case is true					Stops when base case is false
	Created using functions							Created using loops
	Each call requires additional stack memory		Does not require additional memory
	More concise code 								Often requires more code
'''

## EXAMPLE 1A - number addition with a helper function -- we will compare to the recursive function in 1B

#create helper function that adds 1 to an integer

def _add_helper(integer: int):
    return integer + 1

# create parent function that invokes the helper function and adds 2 to the original integer input

def add_parent(n: int) -> int:
    one_more = add_helper(n)
    two_more = add_helper(one_more)
    return two_more

print("Helper version:", add_parent(5))

# Example 1B. Create a recursive version - tail recursion (recursive call is the last thing executed), calculate before next invocation

def add_recursive(n: int, steps: int = 2) -> int:
    if steps == 0:
        return n
    return add_recursive(n + 1, steps - 1)

print("Recursive version:", add_recursive(5))

# Compare to this regular recursive function - unwind the call stack

def add_recursion_regular(integer: int, tracker: int = 2):
    if tracker == 0:
        return integer
    # Make the recursive call first, then use its return value
    result = add_recursion_regular(integer, tracker - 1)
    return result + 1


## EXAMPLE 1B - We can accomplish the same with a more concise recursive formula

def add_recursion(integer: int, tracker: int = 2): # Trackers are not always necessary
    if tracker == 0:  # we use tracker to establish our base case
        return integer
    return add_recursion(integer+1, tracker-1)
print(f'The value returned by add_recursion is:', add_recursion(5))




# EXAMPLE 2A.  Basic example of a summation function using a for-loop

def sum(n):
    result = 0
    for i in range(n + 1):
        result += i
        print(i, result)
    return result

print(sum(10))


## EXAMPLE 2b. Sum using recursion -- using print statements to highlight function calls and then return calculations

def rec_sum(n):
    print(f'Observed: {n}')
    if n == 0:
        print('Base case')
        return 0
    else:
        n += rec_sum(n-1)
    print(f'Returning: {n}')
    return n

print(rec_sum(10))

# Note that a recursive case can be written within a for-loop as well, particularly when dealing with nested information. Below is an example that could be used as a template for summing elements in a nested list.

# sum nested list

def recursive_sum(nested_num_list):
    sum = 0
    for element in nested_num_list:
        if type(element) == type([]):
            sum = sum + recursive_sum(element)
        else:
            sum = sum + element  # captures elements that aren't in a sublist.
    return sum


# '''
# Observe the following recursive problem in https://recursion.vercel.app/
# Note that you will need to enter it by hand - the viz tool doesn't like copied info.

# def fn(n):
#   if n == 0:
#     return n
#   return n + fn(n-1)

# '''

# Example 3. Challenge: calculate the number of legs for a set of spiders - 8 legs per spider

def number_of_spider_legs(num_spiders: int):
    if num_spiders == 1:
        return 8
    else:
        return 8 + number_of_spider_legs(num_spiders-1)
print(number_of_spider_legs(3))

## What this looks like

## STEP 1: number_of _spider_legs(3) -> return 8 + number_of _spider_legs(2) # invokes another call and waits for return value
## STEP 2: number_of _spider_legs(2) -> return 8 + number_of _spider_legs(1) # invokes another call and waits for return value
## STEP 3: number_of _spider_legs(1) -> return 8 base case met, return scalar value
## STEP 4: number_of _spider_legs(2) -> return 8 + 8 #second segment was returned from nested function call (number_spider_legs(1))
## STEP 5: number_of _spider_legs(3) -> return 8 + 16 #second segment was returned from nested function call (number_spider_legs(2))

## Structure of the above

# def number_of_spider_legs(num_spiders: int): # takes one input, we know it must be what we use for our base case
# 	if num_spiders == 1: # our base case is just the number of legs on a single spider
# 		return 8 # we return just 8
# 	else: # if not base case, keep calling function
# 		return 8 + number_of_spider_legs(num_spiders - 1) # we add 8 to return of another call

## Example 4. Challenge: Count elements(recursive) # note control flow statements

## review function using a for-loop to solve

def count(element, lst, index): # index is the starting index
    count = 0
    for i in lst[index:]:
        if i == element:
            count += 1
    return count
print(count(1, [1, 1, 2, 3, 1, 2, 1], 0))

## The recursive equivalent

def count(element, lst, index=0):
    if index >= len(lst):
        return 0
    return (lst[index] == element) + count(element, lst, index + 1) # note that True = 1 and False = 0 in python. index + 1 moves us to next index position



# The recursive equivalent can also be written as:

def count(element, lst, index=0):
    if index >= len(lst):
        return 0
    return (lst[index] == element) + count(element, lst, index + 1) # index + 1 moves us to the next index position


## Example 5. Advanced challenge create a recursive function that calculates the sum of each element in the following
# nested list. Do not use the sum() method. First we will review this written as a for-loop. We use timeit to calculate 

import timeit

start_loop = timeit.default_timer() # returns current time in seconds

lst = [1, 2, [3,4,[5,6,7,[88,8,9,100]]]]
#
def nested_sum_loop(lst):

    sum_loop = 0
    for i in lst:
        if type(i) != list:
            sum_loop = i + sum_loop
        else:
            if type(i) == list:
                for j in i:
                    if type(j) != list:
                        sum_loop = j + sum_loop
                    else:
                        if type(j) == list:
                            for k in j:
                                if type(k) != list:
                                    sum_loop = k + sum_loop
                                else:
                                    if type(k) == list:
                                        for l in k:
                                            if type(l) != list:
                                                sum_loop = l + sum_loop
                                            else:
                                                print('Additional Loops Required')
    return sum_loop

print(nested_sum_loop(lst))

stop_loop = timeit.default_timer()

loop_time  = stop_loop - start_loop

print(f'For-loop time = {loop_time}.')


# TREE RECURSIOON ALTERNATIVE - makes multiple recursive calls per execution. We will compare the compute time as well

start_recursion = timeit.default_timer()

# The follow was adapted from Pythontutor.com

def rsum(L):
    #print(f'Encountered: {L}')
    if type(L) != list: # L is the current list
        return L
    elif L == []: # could also write if len(lst) == 0:
        #print(f'Encountered: []')
        return 0
    else:
        #return rsum(L[0]) + rsum(L[1:])
        sum_return = rsum(L[0]) + rsum(L[1:]) # int + list until list is empty
        #print(f'Returning: {sum_return}.')
    return  sum_return


rsum([1, 2, [3,4,[5,6,7,[88,8,9,100]]]])

stop_recursion = timeit.default_timer()

recursion_time  = stop_recursion - start_recursion

print(f'Recursion time = {recursion_time}.')

print(recursion_time - loop_time) # recursion slightly faster in test run


# TAIL RECURSION - recursive call is the very last operation

def factorial(n, accumulator = 1): # accumulator -> running product; very memory inefficient
    
    # Base Case
    if n == 0:
        return accumulator # accumulator tracks our operation
    
    # Recursive Case - here we multiply first and the result flows forward through the accumulator rather than being calculated backward as the stack unwinds
    return factorial(n - 1, accumulator * n)
    
    
# Recursive alternative to the preceding problem

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# BINARY SEARCH - DIVIDE AND CONQUER RECURSION. left and right refer to the first and last index positions respectively

def binary_search(arr, target, left = 0, right = None):
    if right is None:
        right = len(arr) - 1 # the last index, accounts for zero indexing
   
   # Base Case - empty search range    
   
    if left > right: # this is an invalid search range
        return -1  
        
    mid = (left + right) // 2 # midpoint of arr
    
    if arr[mid] == target: # early termination, success
        return mid
        
    # Recursive case
        
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1) # note adjustment, search space is 0 to mid-1 because we have already searched 1
    else
        return binary_search(arr, target, mid + 1, right)
 
 

### ADDITIONAL PRACTICE PROBLEMS 

## Decreasing triangle

def print_triangle(num_rows: int):
    if num_rows == 1: # base case
        print('*')
    else:
        print(num_rows * '*')
        return print_triangle(num_rows - 1) # child invocation
print(print_triangle(5))

# Increasing triangle (Using tracker variable)

def print_triangle(num_rows: int, tracker: int = 0):
    if tracker < 0:
        return
    else:
        print((num_rows - tracker) * '*')
        return print_triangle(num_rows, tracker - 1)

rows = 5
print_triangle(rows, tracker)

## increasing triangle (without a return)

def print_triangle(num_rows: int):
    if num_rows > 0:
        print_triangle(num_rows - 1) # loops child call
        print(num_rows * '*') # prints out after loops of child call
print_triangle(5)

## min element (recursive)

def min(lst, i, j):
    if len(lst) == 0:
        return
    if i == len(lst) - 1:
        if lst[i] < j:
            return lst[i]
        else:
            return j
    else:

    if lst[i] < j:
        j = lst[i]
    return min(lst, i+1, j)

test_list = [100, 1026, 154189, 1, 5615, 32, -54, 15, 321, 5]
print(min(test_list, 0, test_list[0]))

## alternating prints

def f(n):
    if n > 0:
        f(n-1)
        print('-' * n)
        f(n-1)
f(5)
