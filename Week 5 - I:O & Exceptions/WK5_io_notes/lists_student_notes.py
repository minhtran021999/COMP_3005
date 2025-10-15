
#Quiz

class Dog:
    def __init__(self, sound):
        self.sound = sound
    
    def make_sound(self):
        print(f'A dog goes"{self.sound}"')

dog1 = Dog('woof')

dog1.make_sound()

make a class named Dog. Include an attribute called sound and a method called make_sound the prints out the sound the dog makes. 
Instantiate a dog object and pass 'woof' the class

call the make_sound method through the dog object.




### List Creation ####

lst = []  # square brackets, empty list
print(type(lst))

lst = list()  # list method
print(type(lst))

### Building lists with range() ####

lst = list(range(1, 20, 3))  # list that contains odd values from 1 to 20

print(lst)

## using the .append() method

lst.append('appended')
print(lst)

# ### Slicing lists ####

print(lst[0])  # first element
print(lst[-1])  # last element
print(lst[1:4])  # slice from index 1 to 3, lists are 0 indexed

##### quiz: use slicing to solve #####

# solve the following

lst = [1, 'string', [5, 6, 'str', 67], [45, ('grade', 89)]]

print(lst[3][1][1])  # answer


### Looping over lists - Iteration ####

for var in lst:
    print(var)



### Nested looping

def flatten(lst):
    while True:
        new_lst = []
        has_iterable = False
        for i in lst:
            if isinstance(i, (list, tuple)):
                new_lst.extend(i) # The extend() method in Python is used to add multiple elements at the end of an existing list.
                has_iterable = True
            else:
                new_lst.append(i)
        lst = new_lst
        if not has_iterable: # if false: no more nested lists or tuples are present in lst, so it breaks the while loop
            break
    return lst
print(flatten(lst))


# with exception handling

def flatten(lst):
    if not isinstance(lst, (list, tuple)):
        raise TypeError('Input must be a list or tuple')
    
    while True:
        new_lst = []
        has_iterable = False
        for i in lst:
            if isinstance(i, (list, tuple)):
                new_lst.extend(i)
                has_iterable = True
            else:
                new_lst.append(i)
        lst = new_lst
        if not has_iterable:
            break
    return lst

try:
    lst = [1, 'string', [5, 6, 'str', 67], [45, ('grade', 89)]]
    print(flatten(lst))
except TypeError as e:
    print(e)

