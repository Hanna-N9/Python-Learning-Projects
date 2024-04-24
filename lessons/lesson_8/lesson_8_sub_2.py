# Get A Key
  # Once you have a dictionary, you can access the values in it by providing the key.
  
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", 
                   "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"]) # ['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"]) # ['Aries', 'Leo', 'Sagittarius']


                                      #_______________________________________________________________

# Get an Invalid Key

# Use an if statement to check if "energy" is a key in zodiac_elements. This will return false instead of throwing an error ('KeyError')
if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])
  
  
                                        #_______________________________________________________________

# Safely Get a Key
  # Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you 
  # are trying to .get() does not exist, it will return None by default

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id) # 100019

# Getting a key that doesn’t exist! 
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id) # 100000


                                        #_______________________________________________________________

# Delete a Key
  # Use .pop() to delete a key and we can provide a default value to return if the key does not exist in the dictionary.
  
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, 
                   "power stew": 30}

health_points = 20

# Add the corresponding value of the key "stamina grains" to the health_points variable and remove it from the dictionary. 
# If the key does not exist, add 0 to health_points.
health_points += available_items.pop("stamina grains", 0)

# Add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.pop("power stew", 0)

# Add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to 
# health_points
health_points += available_items.pop("mystic bread", 0)

print(available_items) # {'health potion': 10, 'cake of the cure': 5, 'green elixir': 20, 'strength sandwich': 25}
print(health_points)  # 65


                                        #_______________________________________________________________

# Get All Keys
  # list() function to get all keys
  # A .keys() method that returns a dict_keys object. A dict_keys object is a view object, which provides a look at the current 
  # state of the dictionary, without the user being able to modify anything.
  
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78]}

print(list(test_scores)) 

for student in test_scores.keys():
 print(student)
  
  
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Create a variable called users and assign it to be a dict_keys object of all of the keys of the user_ids dictionary.
users = user_ids.keys()

# Create a variable called lessons and assign it to be a dict_keys object of all of the keys of the num_exercises dictionary
lessons = num_exercises.keys()

print(users)
print(lessons)


                                        #_______________________________________________________________

# Get All Values
  # A .values() method to return a dict_values object with all of the values in the dictionary.

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

# Iterate through the values in the num_exercises dictionary and add each value to the total_exercises variable
for exercises in num_exercises.values():
  total_exercises += exercises

print(total_exercises)


                                        #_______________________________________________________________

# Get All Items
  # Get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list object. 
  # Each element of the dict_list returned by .items() is a tuple consisting of: (key, value)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
  print(f"Women make up {percentage} percent of {occupation}s.")





