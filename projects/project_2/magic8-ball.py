import random

# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
# Write a program that can answer any “Yes” or “No” question with a different fortune each time it executes.

# format
  # [Name] asks: [Question]
  # Magic 8-Ball’s answer: [Answer]

# Setting up 
name = "Joe"
question = "Can this happen in real life?"  # a yes or no question
answer = "" # answer to be given

# Generating a random number
 # use the .randint() function from the random module to generate a random number from a range. Need to import random which is at the top of this file 
random_number = random.randint(1, 9)
# print(random_number)

# Control Flow
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

# Seeing the result
# print(f"{name} asks: {question}")
 # if name is an empty string (no name provided) then print first message else print second message, 
if name == "":
  print(f"Question: {answer}")
else:
  print(f"{name} asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")
