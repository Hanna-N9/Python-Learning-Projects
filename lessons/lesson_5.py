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
    
            #_________________________

# Append => Add an element to the end of a list
orders = ["daisies", "periwinkle"]
print(orders)  # ['daisies', 'periwinkle']

orders.append("tulips")
orders.append("roses")

print(orders) # ['daisies', 'periwinkle', 'tulips', 'roses']

            #_________________________

# Remove => Remove an element from the list
orders.remove("tulips")
print(orders) # ['daisies', 'periwinkle', 'roses']

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


