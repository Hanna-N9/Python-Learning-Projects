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


                                      #_______________________________________________________________

# Add A Key
  # To add a single key: value pair to a dictionary, we can use the syntax: dictionary[key] = value

# Create an empty dictionary
animals_in_zoo = {}

# Add "zebras" to animals_in_zoo as a key with a value of 8.
animals_in_zoo["zebras"] = 8

print(animals_in_zoo)  # {'zebras': 8}

# Add "monkeys" to animals_in_zoo as a key with a value of 12
animals_in_zoo["monkeys"] = 12

# Add "dinosaurs" to animals_in_zoo as a key with a value of 0.
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo) # {'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}
  

                                      #_______________________________________________________________

# Add Multiple Keys
  # If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# Add two users
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids) # {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}


