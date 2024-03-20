# Python built-in function called zip().
  # zip() allows developers to build our programs faster and cleaner by combining associated data sets without relying on 
  # multi-dimensional lists. 
  
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

# Create a nested list that paired each owner with a dog. The zip() function takes two (or more) lists as inputs and 
# returns an object that contains a list of pairs. Each pair includes one element from each of the inputs. 

names_and_dogs_names = zip(owners, dogs_names)

# Object contains the location of this variable in our computer’s memory
print(names_and_dogs_names) # <zip object at 0x101e27500>

# Convert to lists built-in function list()
to_list = list(names_and_dogs_names)
print(to_list) # [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]

  # Converted from zip memory object to an actual list (denoted by [ ])
  # Inner lists don’t use square brackets around the values because they have been converted into tuples (an immutable data type).