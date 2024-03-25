# "Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met."
# "Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size)."

# For Loops: Introduction
  # One of the loop types. It is a form of an definite iteration.


# General Structure of a for loop
  # for <temporary variable> in <collection>:
    #   <action>

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games: 
  print(game) 

for sport in sport_games:
  print(sport)


                                    #_______________________________________________________________
                                    
# For Loops: Using Range

promise = "I will finish the python loops module!"

for temp in range(5): 
  # print(promise)
  print(f"{temp + 1}. {promise}")
  
  
                                      #_______________________________________________________________

# While Loops: Introduction
  # Another type of loop. It is a form of indefinite iteration. A while loop executes instructions if a given condition is true (runs on every iteration until condition becomes false which stops the loop)

# Structure
   # while <conditional statement>:
      # <action>  
      
# While Loop Walkthrough     
count = 0 # initially defined with the value of 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  print("Loop Iteration - count <= 3 is still true")  # Print if the condition is still true
  print("Count is currently " + str(count)) # Print the current value of count 
  count += 1 # Increment count by 1
  print(" ----- ")
print("While Loop ended")


# counts down from 10 to 0(inclusive)
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1 # decrease the value of the countdown variable by 1
print("We have liftoff!") # After the while loop


                                      #_______________________________________________________________

# While Loops: Lists
  # Iterate through a list --- Use the length (len) of the list as the basis for how long the while loop needs to run
  
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0
while index < length:
  print(f"I am learning about {python_topics[index]}") # Like python_topics[0] to access it
  index += 1 
  
  
                                      #_______________________________________________________________

# Infinite Loops

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

# Combine all students from students_period_A into students_period_B
for student in students_period_A:
  # students_period_A.append(student) --- Cause infinite loop due to appending elements from students_period_A to itself, leading to increases in the size of students_period_A with each iteration, causing the loop never to reach its end condition
  print(student)
  students_period_B.append(student)
  print(student)


                                      #_______________________________________________________________

# Loop Control: Break




