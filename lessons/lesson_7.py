# Functions allow tasks to be performed multiple times within a program without being rewritten. For reusability purpose

# Defining a Function

# A function definition --- Function's core in Python
  # The def keyword indicates the beginning of a function (also known as a function header). After the function header is 
  # named in snake_case format that describes the task the function performs. 
    # def function_name():

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")
  
  
                                      #_______________________________________________________________

# Calling a Function
  # "The process of executing the code inside the body of a function is known as calling it (This is also known as “executing a function”)"
  # "To call a function in Python, type out its name followed by parentheses ( )."

# To execute directions_to_timesSq() function
directions_to_timesSq()


                                      #_______________________________________________________________

# Whitespace & Execution Flow
  # "The amount of whitespace tells the computer what is part of a function and what is not part of that function." For this is indentation.

print("Checking the weather for you!")  

def weather_check():
  print("Looks great outside! Enjoy your trip.")
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()


                                      #_______________________________________________________________

# Parameters & Arguments

def generate_trip_instructions(location):
  print(f"Looks like you are planning a trip to visit {location}")
  print(f"You can use the public subway system to get to {location}")

generate_trip_instructions("Grand Central Station")


                                      #_______________________________________________________________

# Multiple Parameters

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate , trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  print(trip_total)

calculate_expenses(200, 100, 100, 5)


                                      #_______________________________________________________________

# Types of Arguments
  # Positional arguments: arguments that can be called by their position in the function definition.
  # Keyword arguments: arguments that can be called by their name.
  # Default arguments: arguments that are given default values.
  
def trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India"):
  print("Here is what your trip will look like!")
  print(f"First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")

trip_planner("Brooklyn", "Queens")


                                      #_______________________________________________________________

# Built-in Functions vs User Defined Functions 
  # Built-in Functions are functions that come built into Python for us to use. User Defined Functions - functions that are written by users

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

#  built-in function max()
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price) # 15.5

#  built-in function min()
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price) # 2.0

# built-in function round()
rounded_price = round(tshirt_price, 1)
print(rounded_price) # 9.8


                                      #_______________________________________________________________

# Variable Access --- to do with scope 

# Global variable
favorite_locations = "Paris, Norway, Iceland"

# This function will print a hardcoded count of how many locations we have.
def print_count_locations():
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations() # There are 3 locations
show_favorite_locations() # Your favorite locations are: Paris, Norway, Iceland


                                      #_______________________________________________________________

# Returns

current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget) # Your remaining budget is: $3500.75


def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt) # Your remaining budget is: $3491.75


                                      #_______________________________________________________________

# Multiple Returns

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

# In order to use our three returned values from top_tourist_locations_italy() we need to assign them to new variables names 
# after we call our function
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1) # Rome
print(most_popular2) # Venice
print(most_popular3) # Florence


                                      #_______________________________________________________________

# Overall of Functions

# Create a function called trip_planner_welcome() that takes one parameter called name
def trip_planner_welcome(name):
  print(f"Welcome to tripplanner v1.0 {name}")

trip_planner_welcome("Jack")

# Define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for
# our user’s trip
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5)

# Create a function called destination_setup() that will have four parameters
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Bali", "Singapore", estimate, "Airplane")


