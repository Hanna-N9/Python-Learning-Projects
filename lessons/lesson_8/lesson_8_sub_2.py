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


