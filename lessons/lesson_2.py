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


