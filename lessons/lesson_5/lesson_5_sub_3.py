# Learn Python: Tuples 
  # Referring a video 'Python Walkthrough Tuples In Python' - https://www.youtube.com/watch?v=yDvRR8nWMNI

# What are tuples?: 

  # A tuple is a data structure that allows developers to store many data types, such as int, string, etc. 
  # It is similar to a list, but a tuple is an immutable data type, meaning that the elements, their order, 
  # and their number can't be changed.
  
  
                                    #_______________________________________________________________
# Creating tuples:

  # Tuples are defined by enclosing the elements in parentheses. Similiar methods to lists but tuples can't be modified.

bunny_info = ("Thumper", "Netherland dwarf", 2, "male") # name, breed type, age, gender
print(bunny_info) # ('Thumper', 'Netherland dwarf', 2, 'male') 

print(bunny_info[1]) # Netherland dwarf

# Unpacking a tuple 
  # assigning the elements of a tuple to individual variables. Must match the number of elements in the tuple
name, breed, age, gender = bunny_info
print(name) # Thumper
print(gender) # male

# If creating a one-element tuple which is a special case
  # Creating a tuple with one item requires adding a comma after the item because parentheses are used for grouping in expressions, 
  # and without the comma, Python would interpret the item as a single value rather than a tuple. So, the trailing comma is 
  # telling Python to recognize it as a tuple.
  
# If ("bunny"), Python would interpret ("bunny") as just the string "bunny" rather than a tuple containing one element
one_element_tuple = ("bunny",) 
print(one_element_tuple ) # ('bunny',) --- stored as a tuple
 
without_tuple = ("bunny") 
print(without_tuple) # bunny


                                    #_______________________________________________________________
# Tuples vs Lists:

  # A list is a mutable data type, while a tuple is an immutable data type, so a tuple doesn't have any unique methods like lists do. 
  # In a list, elements can be added, removed, or modified. Elements cannot be added, removed, or altered in a tuple. Lists are ideal 
  # for collections of elements that need to be modified. Tuples are better suited for collections of items that should not change
