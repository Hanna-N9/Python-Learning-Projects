# If something is True or False (boolean expression)
    
statement_one = "Dogs are mammals."  # This is boolean expression

statement_two = "My dog is named Pavel." # This is boolean expression

statement_three = "Dogs make the best pets." # This is not boolean expression

statement_four = "Cats are female dogs." # This is boolean expression


                                #_______________________________________________________________
                                
# Relational Operators: Equals and Not Equals - (Relational operators compare two items and return either True or False)
    # Equals: ==  |  Not equals: !=

                                #_______________________________________________________________

# Boolean Variables => True and False are the only bool types, and any variable that is assigned one of these values is called a boolean variable.

# Boolean variables - assign True or False to a variable
set_to_true = True
set_to_false = False

# Set a variable equal to a boolean expression - variable contains boolean values

bool_one = 5 != 7  # return True

# bool type vs non bool type

my_baby_bool = "true"

print(type(my_baby_bool)) # <class 'str'>

my_baby_bool_two = True

print(type(my_baby_bool_two)) # <class 'bool'>


                                #_______________________________________________________________

# If statement

# form of a conditional statement --- If [it is raining], then [bring an umbrella] 

# In Python form, instead of “then” we have a colon, :

is_raining = "It is raining" 
if is_raining:  
  print("bring an umbrella")
 
user_name = "John" 
if user_name == "John":
    print(f"The user name, {user_name}, is correct.")
    
    
                                #_______________________________________________________________
                                
# Relational Operators II 
 # two relational operators (==, !=) and four more -- >, >=, <, <=
 
 # A college requires students to earn 120 credits to graduate. Check if the student has enough credits to graduate
 
credits = 120
if credits >= 120:
    print("You have enough credits to graduate!")
     
                                #_______________________________________________________________

# Boolean Operators: and

# and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.

statement_one = "Oranges are a fruit and carrots are a vegetable." # both of which are True and connected by the boolean operator and

# 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher
credits = 120
gpa = 3.4

if gpa >= 2.0 and credits >= 120:
  print("You meet the requirements to graduate!")


                                #_______________________________________________________________
                                
# Boolean Operators: or
# or combines two expressions into a larger expression that is True if either component is True

statement_two = "Oranges are a fruit or apples are a vegetable." # First one is true while second one is false. Because the two expressions are connected by the or operator, the entire statement is True. Only one component needs to be True for an or statement to be True.

print(bool(statement_two)) # True

# Write an if statement that checks if a student either has 120 or more credits or a GPA 2.0 or higher, and if so prints:

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")
  
  
                                #_______________________________________________________________

# Boolean Operators: not
# when applied to any boolean expression it reverses the boolean value. In English is slightly different from the way it would appear in Python because in Python we add the not operator to the very beginning of the statement.

not True == False
not False == True

# college credits and gpa 

credits = 120
gpa = 1.8

# If a student’s credits is not greater or equal to 120
if not credits >= 120:
  print('You do not have enough credits to graduate.')

# If their gpa is not greater or equal to 2.0
if not gpa >= 2.0:
  print('Your GPA is not high enough to graduate.')

# If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0
if not (credits >= 120) and not (gpa >= 2.0):
  print('You do not meet either requirement to graduate!')
  
  
                                  #_______________________________________________________________

# Else Statements
# allow us to describe what we want our code to do when certain conditions are not met.

if age >= 13:
  print("Access granted.")
else:
  print("Sorry, you must be 13 or older to watch this movie.")
  
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")


                                  #_______________________________________________________________

# Else If Statements (elif)
# An elif statement checks another condition after the previous if statements conditions aren’t met. --  additional checks into if statements
  # We can use elif statements to control the order we want our program to check each of our conditional statements. 
    # First, the if statement is checked, then each elif statement is checked from top to bottom
    # then finally the else code is executed if none of the previous conditions have been met.
    
# If $600.00, the code first checks if that is over 1000, which it is not, then it checks if it’s over 500, which it is, so it prints that message, then because all of the other statements are elif and else, none of them get checked and no more messages get printed.

donation = 600

print("Thank you for the donation!")

if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")
# return Thank you for the donation! You've achieved gold donor status


# letter grade

grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
# return B


                                  #_______________________________________________________________

# Overall of Control Flow

# Little Codey is an interplanetary space boxer who is trying to win championship belts for various weight categories on other planets within the solar system.
  # Checking which number planet is equal to.
  # Computing Codey’s weight on the destination planet.
  
  # #	Planet	  Relative Gravity
  # 1	Venus	     0.91
  # 2	Mars	     0.38
  # 3	Jupiter	   2.34
  # 4	Saturn	   1.06
  # 5	Uranus	   0.92
  # 6	Neptune	   1.19
  
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight) # Your weight: 432.9
