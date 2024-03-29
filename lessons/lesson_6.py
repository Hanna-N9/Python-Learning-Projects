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

# Loop Control: Break --- break loop control statements
  # The loop will keep running even when an element exists or matches from the list. So, using a break keyword stop iteration from inside the loop and ends it.

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]

dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break
  

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
print("End of search!")


                                      #_______________________________________________________________

# Loop Control: Continue
  # Situations where we don’t want to end the loop entirely but instead skip the current iteration of the loop
  
# This loop iterates over a list of numbers, skipping any negative numbers. Printing out positive numbers in the list
# When a negative number is encountered, the 'continue' statement is executed, which skips the rest of the loop's body for that iteration and proceeds to the following number. As a result, only positive numbers are printed.
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i <= 0:
    continue
  print(i)
  

# Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)
  
  
                                        #_______________________________________________________________

# Nested Loops --- to loop through each sub-list

#  number of scoops sold for different flavors of ice cream at three different locations
# Sum all the numbers
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

# Loop through each sublist
for location in sales_data:
  print(location)
  # Loop elements in each sublist
  for element in location:
    scoops_sold += element # add the element value to scoops_sold
print(scoops_sold)


                                        #_______________________________________________________________

# List Comprehensions: Introduction

# General Syntax
  # new_list = [<expression> for <element> in <collection>]


# Each element is doubled 
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled) # [4, -2, 158, 66, -90]

# When not using list comprehensions
doubled = []

for number in numbers:
  doubled.append(number * 2) 
print(doubled) # [4, -2, 158, 66, -90]

# ---

# add 10 points to all the grades
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grd +10 for grd in grades]
print(scaled_grades) # [100, 98, 72, 86, 84, 99, 58, 67]


                                        #_______________________________________________________________











