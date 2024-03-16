# Adding by Index: Insert
  # The Python list method .insert() allows us to add an element to a specific index in a list. When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right.
  # The .insert() method takes in two inputs:
    # The index you want to insert into. Numerical index
    # The element you want to insert at the specified index.

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




