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



