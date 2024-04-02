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