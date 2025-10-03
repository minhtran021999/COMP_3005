

'''
We will use this to represent our runtime script

'''

import helper_script 


if __name__ == '__main__':
    
    print(f'\nWe are currently executing a module called {__name__}\n')
    
    print(f'\nWe imported a module called {helper_script.__name__}\n')
    

    # ask user to input an integer value 

    age = int(input('Please enter your age as a number:  '))

    # calculate the square of the users age

    print(f'\nThe square of your age is {helper_script._square_function(age)}\n')