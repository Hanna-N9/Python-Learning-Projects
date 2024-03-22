# "Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met."
# "Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size)."

# For Loops: Introduction
  # one type of loop, a for loop, a type of definite iteration

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

  