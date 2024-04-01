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