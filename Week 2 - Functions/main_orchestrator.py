
'''
We can call all functions at one time using __main__()

'''


##### EXAMPLE 1. SQUARING AN INTEGER #####

def square_integer(value: int):      
    squared_value = value ** 2
    return squared_value
        
        
def _fahrenheit_to_celcius(farenheit: int):      
    return round((fahrenheit -32) * (5/9), 2)


def _celcius_to_fahrenheit(celcius: int):  
    return round((celcius / (5/9) + 32), 2) # round to two decimal places


#### EXAMPLE 2. TEMPERATURE CONVERSION


def convert_temperature(temp: int, current_scale: str):
        
    '''
    Takes helper functions and converts temperature to fahrenheit or celcius
    depending on the unit of measurement for the input. It returns a float          value in the alternate scale.
        
    args:
        temp (int) - actual temperature 
        current_scale (str) - the scale entered (celcius or fahrenheit)
        
    returns:
        (int): temperature converted to alternate scale
        
    '''
    if current_scale.lower() in ('fahrenheit', 'f', 'fahrenheit'):
        return _fahrenheit_to_celcius(temp)
            
    else:
        return _celcius_to_fahrenheit(temp)

def main():

    # Square integer call
    
    print('\nEXAMPLE 1. SQUARING AN INTEGER')
    value = 5
    
    print(f'\nThe square of {5} is {square_integer(value)}.\n')

    # Convert temperature call
    
    print('\nEXAMPLE 2. TEMPERATURE CONVERSION')
    degrees = 43
    
    print(f'\nThe equivalent temperature for {degrees} Fahrenheit in degrees \
    celcius is: {square_integer(degrees)}.\n')
            
if __name__ == '__main__':
    main()