# A dictionary is an unordered set of key: value pairs. It provides us with a way to map pieces of data to each other 
# so that we can quickly find values that are associated with one another.

# Introduction to Python Dictionaries

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors)


                                      #_______________________________________________________________

# Make a Dictionary

# Create a dictionary called translations that maps the following words in English to the words in Spanish
translations = {"mountain": "montaña", "bread": "pan", "friend": "amigo", "horse": "caballo"}


                                      #_______________________________________________________________

# Invalid Keys
   # We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the 
   # dictionary. If we try to, we will get a TypeError.
   # Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. If the key can change, that hash 
   # value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.
   
# Gets an error 'TypeError: unhashable type' --- “unhashable” in this context means that this ‘list’ is an object that can be changed
  # children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}

# Without error
children = {'von Trapp': ['Johannes', 'Rosmarie', 'Eleonore'], 'Corleone': ['Sonny', 'Fredo', 'Michael']}


                                      #_______________________________________________________________

# Empty Dictionary
  # Create an empty dictionary when we plan to fill it later based on some other input.
  
my_empty_dictionary = {}

