#### Week 4 - Class Notes ####


'''
Note for brevity, I have not included complete doc strings in all method definitions

Additionally, I am not using "if __name__ =='__main__:" to orchestrate all of the attribute 
and method calls. You, however, should do this on your homework!

'''

###------------------###
###----- Classes ----###
###------------------###

'''What you should know:

1. Defining & instantiating a class
2. Class syntax
3. Class | instance attributes and methods
4. Inheritance

Vocabulary - see the supplementary materials section in Module 4 for coded examples

Object - An instance of a class. It's a specific realization of the class with actual values.

Instance - Another term for an object. When you create an object from a class, you're "instantiating" the class.

Instance Attribute - A variable that belongs to a specific object. Each instance has its own copy with its own value. Typically defined inside __init__ using self.

Class Attribute - A variable that belongs to the class itself and is shared by all instances of that class. Defined directly in the class body, outside any methods.

Instance Method - A function that belongs to a specific object and can access and modify that object's instance attributes. Takes self as its first parameter.

Class Method - A method that belongs to the class itself rather than instances. Takes cls as its first parameter and is decorated with @classmethod. It can access and modify class attributes.

Static Method - A method that belongs to a class but doesn't access instance or class attributes. Decorated with @staticmethod and doesn't take self or cls as a parameter.

__init__ method - The constructor or initializer method. It's automatically called when you create a new instance and is used to set up initial instance attribute values.

self - A reference to the current instance of the class. Used inside instance methods to access that object's attributes and methods.

Dot notation - The syntax used to access attributes and methods using a period, like object.attribute or ClassName.class_attribute.

Instantiation - The process of creating an object from a class using the class name followed by parentheses.
    
    
'''

###---------------------------------------###
###----- Python Class Objects ------------###
###---------------------------------------###

##### Example 1. Instantiate a Class

class ClassDemo:
    pass


print(ClassDemo) # returns default string of the class object, <class '__main__.ClassDemo'>



##### Example 2. Class Functionality: What's inside a Python Class object #####

builtin_num= 0
for builtin in dir(ClassDemo):
    builtin_num += 1
    print(builtin)

print(f'The number of built-in methods and attributes in a base Python class is: {builtin_num}.')


##### Example 3. Update the Class to Include a DocString #####

class ClassDemo:

    '''
    This class demonstrates the creation of instance attributes & methods using Python buitins

    Attributes:
        None - (replace with attribute name, type, and purpose)

    Methods:
        None - (replace with method name, type and purpose)
        
    '''



print(ClassDemo.__doc__) # __doc__ is a dunder attribute -> refers to data, not a method, access via class name using dot notation


###-----------------------------------------###
###----- Python Class Instances ------------###
###-----------------------------------------###


#### Example 4. Instance of a class --> class as a blueprint #####


# Instantiation is the process of creating an object from a class. An object is an instance of a class.

# The class is the blueprint for the object.

# self is a reference to the instance of the class that is being created. Self enables the instance to access attributes and methods that belong to the class. 
# self is included as the first argument in the class definition.
# self also enables us to attach attributes to an instance


class_instance = ClassDemo()


# The instance has the same functionality as the class from which it is derived

builtin_num = 0
for builtin in dir(instance_object):
    builtin_num += 1
    print(builtin)
print(f'The number of builtins and methods in the class instance is: {builtin_num}')


# Example 5. Update Class to include instance methods and attributes ######

class ClassDemo:

    '''
    This class demonstrates the creation of instance attributes & methods using Python buitins
    
    Attributes:
        class_section (str): day of week the class section is taught
        student_name (str): student's first and last name
        student_id (str): student's unique university identification
        student_status (str): student's current enrollment status, 'active' or 'inactive'

    Methods:
        student_record (str): combination of student name, ID, and class section
        activate_student (): updates student status to 'active' if class_section is assigned
    '''

    #Class constructor to iniatialize instance object. Assigns values to instance attributes -> Data

    def __init__(self, student_name, student_id, class_section=None):
        """docstring here"""

        # Instance Attributes 
        
        self.class_section = class_section
        self.student_name = student_name
        self.student_id = student_id
        
        # Default status
        self.student_status = "Inactive"
        
        # activate_student method call -> this is an action or execution of the instance method, not the method itself
        
        self.activate_student()
        
    # Instance Methods
        
    def student_record(self):
        print(f'Student Name: {self.student_name}, Student ID: {self.student_id}, Student Class Section: {self.class_section}')
            
    def activate_student(self):
        if self.class_section is not None:
            self.student_status = "active"

instance_object = ClassDemo("Thursday", "Sarah Keller", "09675434") #


# # Has this changed the Instance & Class Object?

builtin_num = 0
for builtin in dir(instance_object):
    builtin_num += 1
    print(builtin)
print(f'The number of builtins and attributes/methods in the class instance is: {builtin_num}')

# Access the Instance attributes and records

print(instance_object.student_name)

instance_object.student_record()

print(instance_object.student_status)

print(instance_object.__doc__)



###-----------------------------------------------------###
###----- Combining Class and Instance Functionality ----###
###-----------------------------------------------------###


# Example 6. Let's create a class that takes in a list of data and returns the total count of values in the data and the total number of instances.

class CreateData:
    """
    A class used to manage a dataset and track the number of instances created.

    Class Attributes:
        _instance_count (int): The number of instances of the class that have been created.

    Instance Attributes:
        data (list): The dataset that the instance manages.

    Class Methods:
        get_instance_count(cls): Prints the total count of instances.

    Instance Methods:
        
        count_data_values(self): Returns the total count of values in the data.
    """

    # "Class attribute" to keep track of the number of instances - class attributes are shared by all instances of the class. Defined outside of __init__

    _instance_count = 0 # shared by all instances, the leading underscore _ indicates that this is an internal attribute

    # init constructor - called when a new instance is created, initializes attributes of the object

    def __init__(self, data): # initializes a newly created instance

         # Initialize the instance attribute, data, with the provided data
        self.data = data #self.data refers to the new instance, data (right side) refers to the data passed in as a parameter

        # Class attribute, increments the instance count each time an instance is created, ignores the local instance (self) and goes to classes namespace
        CreateData._instance_count += 1 # This is an operation on _instance_count. It is not an attribute or method. located within init to execute when an instance is created.

    def count_data_values(self): # instance method that counts # of items in the dataset
        return len(self.data)

    @classmethod # method is bound to the class but callable from class as well as instance

    def get_instance_count(cls):
        # Print the total count of instances
        print(f'Total count of instances: {cls._instance_count}')


# Create three instances of the CreateData class

data1 = CreateData([1, 2, 3])

# Attribute check (Direct Access)

CreateData._instance_count

data2 = CreateData([4, 5, 6])

data3 = CreateData([7, 8, 9, 5, 6, 7])

# Class method call via. instance or class

data3.get_instance_count()

CreateData.get_instance_count()

''' Note: we cant call instance methods from the class itself -> CreateData.count_data_values() # generates a type error'''



###--------------------------------###
###----- Class Inheritance --------###
###--------------------------------###

# Example 7. Method Resolution Order 

'''
When you access a method or attribute from a class instance (e.g., my_instance.attribute), 
Python performs a lookup in the following sequence until it is found:

instance -> instance class -> inherited parent classes -> base class (object)

Note: every Python class inherits from object, which provide the default implementation of class
methods/attributes. 

If the attribute or method isnt found in this hierarchy, an AttributeError results.

'''


class Parent:
    pass
    
class child(Parent):
    pass
    
print(child.__mro__)



class DataProcessor(CreateData): # inherits from CreateData (parent class)
    """
    Manages and processes a student's record and status, inheriting core data
    handling functionality from CreateData.

    Attributes:

        description (str): A description of the dataset being processed.

    Methods:

        get_description(): Prints the description of the dataset.
        
        full_summary(): Combines inherited and new functionality, printing the description
                         and the total count of data elements.
        
    """

    def __init__(self, data, description):
        """

        """
        

        # Call the __init__ method of the parent class (CreateData)

        super().__init__(data) # calls the parent class init method, passes in data to CreateData.__init__()

        # Initializes new attribute specific to the subclass

        self.description = description

    # Attribute methods

    def get_description(self):
        """Prints the description of the dataset."""
        print(f"Dataset Description: {self.description}")

    def full_summary(self):
        """Combines inherited and new functionality."""
        print(f"Data set: {self.description}")
        print(f"Total elements: {self.count_data_values()}") # Inherited method





description = "this is a description of the data"

data_obj = DataProcessor([5,6,7,888,99], description) # initializes instance of the DataProcessor class

data_obj.full_summary()



### THURSDAY SECTION NOTE ---> output of None in addition to the summary
'''
If you recall, I used the following print command
print(data_obj.full_summary())

This causes the the summary text (description) and total # of items in the dataset to be printed. 
Because our instance method, full_summary(), doesnt include an explicit return statement, it returns None

To avoid this, call: data_obj.full_summary(), None won't be printed 

'''



