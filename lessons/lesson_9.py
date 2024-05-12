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