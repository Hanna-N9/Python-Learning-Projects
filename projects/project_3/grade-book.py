# This program is for a student to organize subjects and grades 

# Create Some Lists:

# Create a list called subjects and fill it with the classes you are taking:
subjects = ["physics", "calculus", "poetry", "history"]

# Create a list called grades and fill it with your scores:
grades = [98, 97, 85, 88]

# Create a two-dimensional list to combine subjects and grades.
gradebook = [
  ["physics", 98], ["calculus",	97], ["poetry",	85], ["history", 88]
]
print(gradebook) # [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

# Add More Subjects:

# Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook
gradebook.append(["computer science", 100])

# Use append to add ["visual arts", 93] to gradebook
gradebook.append(["visual arts", 93])
print(gradebook)  # [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100], ['visual arts', 93]]

# Modify The Gradebook:

# Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class. Access the index of the grade for your visual arts class and modify it to be 5 points greater
gradebook[-1][-1] += 5
print(gradebook)  # [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100], ['visual arts', 98]]

# Switch from a numerical grade value to a Pass/Fail option for your poetry class. Use the .remove() method to delete it
gradebook[2].remove(85)
# Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located
gradebook[2].append("Pass")
print(gradebook)  # [['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98]]

# One Big Gradebook!

# You also have your grades from last semester, stored in last_semester_gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook) # [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65], ['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98]]


