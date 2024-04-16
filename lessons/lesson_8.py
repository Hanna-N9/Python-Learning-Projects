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


                                      #_______________________________________________________________

# Overwrite Values
  # Our value assignment can overwrite the existing value attached to its key.

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight" 


                                      #_______________________________________________________________

# Dict Comprehensions
  # Supposedly we have two lists that we want to combine into a dictionary.
  # Python allows you to create a dictionary using a dict comprehension, with this syntax:
    # <variable-name> = {key:value for key, value in zip(<key>, <value>)}
  # zip() combines two lists into an iterator of tuples with the list elements paired together.

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.
zipped_drinks = zip(drinks, caffeine)

# Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through the zipped_drinks iterator and 
# turns each tuple pair into a key:value item.
drinks_to_caffeine = {key:value for key, value in zipped_drinks}





