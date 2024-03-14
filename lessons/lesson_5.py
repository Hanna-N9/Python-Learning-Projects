#  In Python, a list is one of the many built-in data structures that allows us to work with a collection of data in sequential order.

# List can contain integer, string, boolean, float as well as combining multiple data types. They can be stored into a list with a square brackets.
heights = [61, 70, 67, 64]
names = ["Noelle", "Ava", "Sam", "Mia"]
mixed_list_common = ["Mia", 27, False, 0.5]

                                    #_______________________________________________________________
                                    
# Emtpy Lists => A list doesn’t have to contain anything.
 # This is if we want to fill it up later based on some other input

my_empty_list = []

                                    #_______________________________________________________________

# List Methods
  # Built-in functionality to create, manipulate, and delete data
    # Methods will follow the form of list_name.method()
    
                                    #_______________________________________________________________

# Append => Add an element to the end of a list
orders = ["daisies", "periwinkle"]
print(orders)  # ['daisies', 'periwinkle']

orders.append("tulips")
orders.append("roses")

print(orders) # ['daisies', 'periwinkle', 'tulips', 'roses']


                                    #_______________________________________________________________

# Growing a List: Plus (+)
  # When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).
  # Need to create a new variable to have both the original items sold, and the new items in square brackets
  # Original variable doesn't change
  
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = orders + ["lilac", "iris"]
print(new_orders)  # ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily', 'lilac', 'iris']

# Combine orders and new_orders
orders_combined = orders + new_orders
print(orders_combined) # ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily', 'daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily', 'lilac', 'iris']

# Causes error if not in square brackets
 #broken_prices = [5, 3, 4, 5, 4] + 4

# Fix the error 
 broken_prices = [5, 3, 4, 5, 4] + [4]
 

                                    #_______________________________________________________________

# Accessing List Elements
  # We call the location of an element in a list its index. Lists are zero-indexed
  # Select a single element from a list by using square brackets and the index of the list item (int). Example, orders[2] outputs snapdragon

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]

print(employees[5]) # Andy

                                    #_______________________________________________________________

# Accessing List Elements: Negative Index
  # Select the last element of a list by index -1
  
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
print(last_element) # cereal
index5_element = shopping_list[5]
print(index5_element) # cereal

                                    #_______________________________________________________________

# Modifying List Elements
   # Change a value in a list, reassign the value using the specific index.

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
print(garden_waitlist) # ['Jiho', 'Adam', 'Sonny', 'Alisha']

# Replace with another customer 
garden_waitlist[1] = "Calla"
print(garden_waitlist) # ['Jiho', 'Calla', 'Sonny', 'Alisha']

# Replace with another customer 
garden_waitlist[-1] = "Alex"
print(garden_waitlist) # ['Jiho', 'Calla', 'Sonny', 'Alex']
 
                                    #_______________________________________________________________

# Shrinking a List: Remove 


order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list) # ['Celery', 'Orange Juice', 'Orange', 'Flatbread']

order_list.remove("Flatbread")
print(order_list) # ['Celery', 'Orange Juice', 'Orange']


new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list) # ['Celery', 'Orange Juice', 'Orange', 'Flatbread']

# Only the first instance of the matching element is removed
new_store_order_list.remove("Mango")
print(new_store_order_list) # ['Orange', 'Apple', 'Broccoli', 'Mango']

                                    #_______________________________________________________________

# Two-Dimensional (2D) Lists

# A 2d list with two lists in each of the indices.
heights = [
  ["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]
]

ages = [
  ["Aaron", 15], ["Dhruti", 16]
]

                   #_______________________________________________________________

# Accessing 2D Lists by using double square brackets

class_name_test = [
  ["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]
]
print(class_name_test) # [['Jenny', 90], ['Alexus', 85.5], ['Sam', 83], ['Ellie', 101.5]]

sams_score = class_name_test[2][1]
print(sams_score) # 83

ellies_score = class_name_test[-1][-1]
print(ellies_score) # 101.5

# Element	       Index
# "Jenny"	    heights[0][0]
# 90	        heights[0][1]
# "Alexus"    heights[1][0]
# 85.5	      heights[1][1]
# "Sam"	      heights[2][0]
# 83	        heights[2][1]
# "Ellie"	    heights[3][0]
# 101.5	      heights[3][1]

                   #_______________________________________________________________

# Modifying 2D Lists => reassign the value using the specific index

incoming_class = [
  ["Kenny", "American", 9], ["Tanya", 	"Ukrainian", 9], ["Madison", "Indian", 7]
]
print(incoming_class) # [['Kenny', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 7]]

# Positive indices
incoming_class[2][2] = 8
print(incoming_class)  # [['Kenny', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 8]]

# Negative indices
incoming_class[-3][-3] = "Ken"
print(incoming_class)  # [['Ken', 'American', 9], ['Tanya', 'Ukrainian', 9], ['Madison', 'Indian', 8]]

                   #_______________________________________________________________

# Overall of Lists

# Your code below: 

first_names = ["Ainsley", "Ben", "Chani", "Depak"]

# Customer’s preferred sizes 
preferred_size = ["Small", "Large", "Medium"]

# Depak’s size
preferred_size.append("Medium")
print(preferred_size) # ['Small', 'Large', 'Medium', 'Medium']


# Two-dimensional list - name, size, expedited shipping on orders (True for expedited, False for regular)
customer_data = [
  ["Ainsley", "Small",	True], ["Ben", "Large",	False], ["Chani",	"Medium",	True], ["Depak",	"Medium",	False]
]
print(customer_data) # [['Ainsley', 'Small', True], ['Ben', 'Large', False], ['Chani', 'Medium', True], ['Depak', 'Medium', False]]

# Change data value for "Chani"‘s shipping preference to False
customer_data[2][2] = False

# Remove Ben's shipping option (the True or False value) 
customer_data[1].remove(False)

# Two new customers 
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final) # [['Ainsley', 'Small', True], ['Ben', 'Large'], ['Chani', 'Medium', False], ['Depak', 'Medium', False], ['Amit', 'Large', True], ['Karim', 'X-Large', False]]

