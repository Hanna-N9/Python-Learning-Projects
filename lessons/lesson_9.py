# Types
  # Python equips us with many different ways to store data. Like int, float, string, list, dict and so on...
  # Use the type() function to check the type of a Python data.

# Call type() on the integer 5 and print the results.
print(type(5)) # <class 'int'>


# Define a dictionary my_dict using curly braces {}.
my_dict = {}
print(type(my_dict)) # <class 'dict'>


# Define a list called my_list
my_list = []
print(type(my_list)) # <class 'list'>


                                    #_______________________________________________________________

# Class
  # A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will 
  # interact with that data. 
  # Define a class using the class keyword. 
  # PEP 8 Style Guide for Python Code recommends capitalizing the names of classes to make them easier to identify.

# Define an empty class called Facade. 
class Facade:
    pass

class CoolClass:
    pass


                                    #_______________________________________________________________

# Instantiation
  # A class doesn’t accomplish anything simply by being defined. A class must be instantiated. In other words, 
  # we must create an instance of the class, in order to breathe life into the schematic.
  
  # Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined CoolClass as follows:
cool_instance = CoolClass()

# Above, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable 
# cool_instance for safe-keeping so we can access our instance of CoolClass at a later time

# Make a Facade instance and save it to the variable facade_1
facade_1 = Facade()


                                    #_______________________________________________________________

# Object-Oriented Programming
  # A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities
  # of a program is known as Object Oriented Programming or OOP.
  
# Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, 
# it returns the class that the object is an instance of.
print(type(cool_instance)) # "<class '__main__.CoolClass'>"

# When printing out the type() of cool_instance, it shows that this object is of type __main__.CoolClass. In Python __main__ means the 
# current script/file itself is being executed/running. One could read the output from type() to mean, the CoolClass is the class that is 
# defined within the current script file.

facade_1_type = type(facade_1)
print(facade_1_type) # <class '__main__.Facade'>


                                    #_______________________________________________________________

# Class Variables
  # A class variable is a variable that’s the same for every instance of the class. You can define a class variable by including it in 
  # the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.
  # Class variables are often referenced with a leading period, like .title above. This is done to quickly show that the variable belongs
  # to a class and must be accessed with dot notation, like drummer.title.

class Musician:
  title = "Rockstar" # class variable

drummer = Musician() # instantiated
print(drummer.title) # prints "Rockstar"


# Create a Grade class with a class attribute .minimum_passing equal to 65.
class Grade:
  minimum_passing = 65
  
  
                                    #_______________________________________________________________

# Methods
  # Methods are functions that are defined as part of a class. The first argument in a method is always the object that is calling the 
  # method. Convention recommends that we name this first argument self. Methods always have at least this one argument.
  # We define methods similarly to functions, except that they are indented to be part of the class
  
  # When calling a method, the self parameter isn't explicitly passed by the programmer. Instead, Python automatically provides the 
  # current instance of the class as the first argument to the method. To put it simply, Python manages the self part internally, ensuring 
  # it's implicitly passed

class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

# Above we created a Dog class with a .time_explanation() method that takes one argument, self, which refers to the object calling the 
# function. We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object for Pipi.

# Notice we didn’t pass any arguments when we called .time_explanation(), but were able to refer to self in the function body. When you call
# a method it automatically passes the object calling the method as the first argument.

# Create a class and method
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."


                                    #_______________________________________________________________

# Methods with Arguments
  # Methods can also take more arguments than just self.

# Calculates the area of a circle
class Circle:
  pi = 3.14
  
  def area(self, radius):
    return self.pi * radius ** 2
  
circle = Circle() # Create an instance of Circle

# Measure several circles 
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)


                                    #_______________________________________________________________

# Constructors -- Common ones with __init__
  # dunder methods is two underscores (double-underscore abbreviated to “dunder”) on either side of methods.
    # First dunder method we’re going to use is the __init__() method (two underscores before and after the word “init”). This method is
    # used to initialize a newly created object. It is called every time the class is instantiated.
    # Methods that are used to prepare an object being instantiated are called constructors. Constructor is usually referring to the 
    # __init__() method.

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")
  
teaching_table = Circle(36) # New circle with diameter: 36


class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter() # "HELLO?!"


class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
      print(phrase.upper())

shout1 = Shouter("shout") # SHOUT


                                    #_______________________________________________________________

# Instance Variables
  # A class is a schematic for a data type and an object is an instance of a class. Each instance of a class can hold different kinds of
  # data. The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class —
  # they are variables that are specific to the object they are attached to.
  
class Store:
  pass

# Create two objects from this Store class
alternative_rocks = Store()
isabelles_ices = Store()

# Assigning the store_name attribute to each instance 
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

print(alternative_rocks.store_name)  # Output: Alternative Rocks
print(isabelles_ices.store_name)  # Output: Isabelle's Ices

# Above is not a bad practice, but it is better to use __init__ method for better readability .


class Dog:
    def __init__(self, name, age): # constructor
        self.name = name  # Instance variable
        self.age = age   # Instance variable

# Creating instances of the dog class
dog_1 = Dog("Buddy", 2)
dog_2 = Dog("Luna", 7)

# Accessing instance variables
print(dog_1.name)  # Output: Buddy
print(dog_1.age)   # Output: 2
print(dog_2.name)  # Output: Luna
print(dog_2.age)   # Output: 7


                                    #_______________________________________________________________
# Attribute Functions
  # Instance variables and class variables are both accessed similarly in Python. They are both considered attributes of an object. 
  # If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an 
  # AttributeError. 
  
  # What if we aren’t sure if an object has an attribute or not? hasattr() will return True if an object has a given attribute and 
  # False otherwise. If we want to get the actual value of the attribute, getattr() is a Python function that will return the value of a 
  # given object and attribute. In this function, we can also supply a third argument that will be the default if the object does not have 
  # the given attribute.

# The syntax and parameters for these functions look like this:

# hasattr(object, “attribute”) has two parameters:
  # object : the object we are testing to see if it has a certain attribute
  # attribute : name of attribute we want to see if it exists

# getattr(object, “attribute”, default) has three parameters (one of which is optional): 
  # object : the object whose attribute we want to evaluate
  # attribute : name of attribute we want to evaluate
  # default : the value that is returned if the attribute does not exist (note: this parameter is optional)

class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!") # prints "This text gets printed!"

# if the attributeless object has the attribute .fake_attribute. Since it does not, hasattr() returned False. 
hasattr(attributeless, "fake_attribute") # returns False

# Since .other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800
getattr(attributeless, "other_fake_attribute", 800) # returns 800, the default value

getattr(dog_1, "name", 800) # returns Buddy


#  a list of different data types: a dictionary, a string, an integer, and a list
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

# For every element in can_we_count_it, check if the element has the attribute .count using the hasattr() function, else
for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")


                                    #_______________________________________________________________

# Self

# In Circle‘s constructor, set the instance variable self.radius to equal half the diameter that gets passed in.

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    
    self.radius = diameter / 2
  
  # Returns the circumference of a circle with the given radius by this formula: circumference = 2 * pi * radius
  # Use self to refer to class and instance variables
  def circumference(self):
    return 2 * self.pi * self.radius

# Define three Circles (instances of Circles) with three different diameters.
medium_pizza = Circle(12) # Creating circle with diameter 12
teaching_table = Circle(36) # Creating circle with diameter 36
round_room = Circle(11460) # Creating circle with diameter 11460

# Print out the circumferences of medium_pizza, teaching_table, and round_room
print(medium_pizza.circumference()) # 37.68
print(teaching_table.circumference()) # 113.04
print(round_room.circumference()) # 35984.4






