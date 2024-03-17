# Initial data
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list) # ['Mango', 'Filet Mignon', 'Chocolate Milk']

# After inserting Pineapple in front of the list
front_display_list.insert(0, "Pineapple")
print(front_display_list) # ['Pineapple', 'Mango', 'Filet Mignon', 'Chocolate Milk']

                                    #_______________________________________________________________

# Removing by Index: Pop
  # Remove elements at a specific index using a method called .pop()
  # Using .pop() without an index will remove whatever the last element of the list is.
  # The .pop() method takes an optional single input: 
    # The index for the element you want to remove.

# Initial data
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics) # ['Machine Learning', 'SQL', 'Pandas', 'Algorithms', 'Statistics', 'Python 3']

# Use .pop() method
data_science_topics.pop()
print(data_science_topics) # ['Machine Learning', 'SQL', 'Pandas', 'Algorithms', 'Statistics']

data_science_topics.pop(3)
print(data_science_topics) # ['Machine Learning', 'SQL', 'Pandas', 'Statistics']

                                    #_______________________________________________________________

# Consecutive Lists: Range
  # A built-in function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input
  # The range() function is unique in that it creates a range object. In order to use this object as a list, we have to first convert it using another built-in function called list().
   # list() function takes in a single input for the object you want to convert
  
# range() function
number_list = range(9)
print(number_list) # range(0, 9)

# list() function
print(list(number_list)) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

zero_to_seven = range(8)
print(list(zero_to_seven)) # [0, 1, 2, 3, 4, 5, 6, 7]

                                    #_______________________________________________________________

# The Power of Range!
  # By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.
  # If we use a third input, we can create a list that “skips” numbers.
  
my_list = range(2, 9)
print(list(my_list)) # [2, 3, 4, 5, 6, 7, 8]

# Starts at 5, Has a difference of 3 between each item, Ends before 15
range_five_three = range(5, 15, 3)
print(list(range_five_three)) # [5, 8, 11, 14]

range_diff_five = range(0, 40, 5)

                                    #_______________________________________________________________

# Length 
  # a built-in function called len()

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", 
             "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

long_list_len = len(long_list)
print(long_list_len) # 18

# ---- 

big_range = range(2, 3000, 10)

big_range_length = len(big_range)
print(big_range_length) # 300

# ---- 

big_range = range(2, 3000, 100)

big_range_length = len(big_range)
print(big_range_length) # 30

                                    #_______________________________________________________________

# Slicing Lists I
  # We want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing
  # Syntax <variable>[start:end]. Count by index
    # start is the index of the first element that we want to include in our selection
    # end is the index of one more than the last index that we want to include. index + 1
    
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]
print(beginning) # ['shirt', 'shirt', 'pants', 'pants'

beginning = suitcase[0:2]
print(beginning) # ['shirt', 'shirt']

middle = suitcase[2:4]
print(middle) # ['pants', 'pants']

                                    #_______________________________________________________________

# Slicing Lists II
  # If we want to select the first n elements of a list, we could use the following code: <variable>[:n]
    # print the elements from initial index, but not including, the element at index n
  # <variable>[-n:] leads to starting from the last index up to the end of the sequence
  # <variable>[:-n] leads to taking all but n last elements of a list

# First 3 elements
print(suitcase[:3]) # ['shirt', 'shirt', 'pants']

# Last 2 elements
last_two_elements = suitcase[-2:]
print(last_two_elements) # ['pajamas', 'books']

# Containing all but the last three elements
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three) # ['shirt', 'shirt', 'pants']# 

                                    #_______________________________________________________________

# Counting in a List
  # Count occurrences of an item in a list. A method called .count()
  
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", 
         "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie",
         "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

jake_votes = votes.count("Jake")
print(jake_votes) # 9

# ---- 

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]

num_pairs = number_collection.count([100, 200])
print(num_pairs) # 2

                                    #_______________________________________________________________
                                    
# Sorting Lists I
  # Method .sort()
  # <variable>.sort(reverse=True) in descending order
  
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace",
             "1600 Pennsylvania Ave", "10 Downing St."]

addresses.sort()
print(addresses) # ['10 Downing St.', '12 Grimmauld Place', '1600 Pennsylvania Ave', '221 B Baker St.', '42 Wallaby Way', '742 Evergreen Terrace']

# ---- 

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]

# The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. If we assign the method's result, it will assign the value None to the variable.
sorted_cities = cities.sort()
print(sorted_cities) # None

cities.sort(reverse=True)
print(cities) # ['Rome', 'Paris', 'New York', 'Los Angeles', 'London']

                                    #_______________________________________________________________

# Sorting Lists II
  # A built-in function sorted()
  # The sorted() function is different from the .sort() method in two ways:
    # It comes before a list, instead of after as all built-in functions do.
    # It generates a new list rather than modifying the one that already exists.

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

print(games) # ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games_sorted) # ['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']

                                    #_______________________________________________________________

# Overall of Working with Lists

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser",
             "dresser", "table", "table", "nightstand", "nightstand", "king bed", 
             "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Length
inventory_len = len(inventory)
print(inventory_len) # 19

# Select the first element in inventory
first = inventory[0]
print(first) # twin bed

# Select the last element from inventory
last = inventory[-1]
print(last) # pillow

# Select items from the inventory starting at index 2 and up to, but not including, index 6
inventory_2_6 = inventory[2:6]
print(inventory_2_6) # ['headboard', 'queen bed', 'king bed', 'dresser']

# Select the first 3 items of inventory
first_3 = inventory[:3]
print(first_3) # ['twin bed', 'twin bed', 'headboard']

# How many 'twin bed's are in inventory?
twin_beds = inventory.count("twin bed")
print(twin_beds) # 4

# Remove the 5th element in the inventory
removed_item = inventory.pop(4)
print(removed_item) # king bed

# There was a new item added to our inventory called "19th Century Bed Frame". Use the .insert() method to place the new item as the 11th element in our inventory.
inventory.insert(10, "19th Century Bed Frame")

# Sort inventory using the .sort() method or the sorted() function
inventory.sort()

# Sort inventory using the .sort() method or the sorted() function. Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().
inventory.sort()









 




