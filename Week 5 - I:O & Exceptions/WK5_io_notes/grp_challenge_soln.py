'''
WEEK 5 - Group Challange


Assign a class coder who will code your solution and share it after our time is complete.  

Create a class called ‘Vehicle’ that includes the following attributes: color, year, make, model, top_speed, mpg, and tank_capacity.

Create a private helper method called “_validate_positive_number” that has three parameters (value, attribute name, is_integer). Note that 'is_integer' is a default parameter (boolean). 

The method should include exception handling (try/except, raise) and conditional statements to validate whether an attribute value is an integer or float and whether it is a positive value. A user should be notified of the relevant error. 

***For the purposes of clarity I suggest that you include the helper method before the attributes in order of sequence. Attributes that have numerical values should be defined using the “validate_positive_number” method. 
For example: temp_celcius = validate_positive_number(some parameters)***

Include a method called “vehicle_range_miles” to calculate and return the vehicle’s maximum driving range. The vehicle is a gas vehicle. Be sure to check again for non-positive values and notify the user if an error is detected. 

Create an instance of the class using: Vehicle('red', 1955, 'Chevrolet', 'Bel Air', 132, 13.3, 12)

Time permitting, test your code with 'edge' cases

GOALS:

- Apply exception handling in a strategic manner 
- Verify attribute types as they are instantiated
- Further integration of Python-based concepts and skills 

'''

# Code solution that I used in the Tuesday/Thursday sections with minor simplifications. The goals of this 

class Vehicle:
    """
    Class Vehicle creates a vehicle object, simplified for gas engines
    Attributes:
    ----------------------------------------
        color (str): vehicle's color
        year (int): the year when the vehicle was manufactured
        make (str): the vehicle's manufacturer
        model (str): the vehicle's model
        top_speed (float): top speed the vehicle can reach (in miles/hour)
        mpg (float): vehicle's fuel use (miles per gallon)
        tank_capacity (float): vehicle's tank capacity (gallons)
    Method:
    ----------------------------------------
        vehicle_range_miles: Returns a float which is the total range of the vehicle
    """
    
    # This private helper function consolidates validation to avoid repeated try-except blocks for the attributes
    
    def _validate_positive_number(self, value, attribute_name, is_integer=False): 
        """Helper method for unified validation and error raising."""
        try:
            
            # Attempt conversion -> see attributes, Year will be an int other numerical data will be float
            validated_value = int(value) if is_integer else float(value) # this is a ternary operator: if is_integer is true the expression evaluates to int(value), otherwise it evaluates to float(value)  
            if validated_value <= 0:
                raise ValueError(f"The '{attribute_name}' must be a positive number.")
                
            return validated_value
            
        # Failed conversions     
        except (TypeError, ValueError) as e:  # e is an alias/var assigned to the exception. It represents a specific exception object
            
           # Re-raise if it's our custom ValueError from the try block
            if isinstance(e, ValueError) and "positive number" in str(e):
                raise  
            
            # Otherwise, raise TypeError due to conversion failure -- updated to be easier to read 
            else:
                raise TypeError(
                    f"The '{attribute_name}' must be {'an integer' if is_integer else 'a number'}"
                    f"(received: {type(value).__name__}).") # gives input value type in readable form ('str') via. __name__. Otherwise we get the name object e.g., <class 'str'>
            
    
    def __init__(self, color: str, year, make: str, model: str, top_speed, mpg, tank_capacity):
        # Assigning Attributes (with validation)
        self.color = color
        self.year = self._validate_positive_number(year, 'year', is_integer=True) # if a year is entered as a float, this will reset it to an int
        self.make = make
        self.model = model
        self.top_speed = self._validate_positive_number(top_speed, 'top_speed')
        self.mpg = self._validate_positive_number(mpg, 'mpg')
        self.tank_capacity = self._validate_positive_number(tank_capacity, 'tank_capacity')
        
    
    def vehicle_range_miles(self) -> float:
        """
        Returns the total range of the vehicle (miles).
        """
        # Defensive check against external modification to non-positive values
        if self.mpg <= 0 or self.tank_capacity <= 0:
            raise ValueError("Cannot calculate range: 'mpg' and 'tank_capacity' must be greater than zero.")

        vehicle_range = round(self.mpg * self.tank_capacity, 2)
        return vehicle_range

        
if __name__ == '__main__':
    
    instance = Vehicle('red', 1955, 'Chevrolet', 'Bel Air', 132, 13.3, 12)
    print(f'\nOur vehicle color is: {instance.color}\n')
    print(f"Our vehicle's driving range is {instance.vehicle_range_miles()} miles.\n")