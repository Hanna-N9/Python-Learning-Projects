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








