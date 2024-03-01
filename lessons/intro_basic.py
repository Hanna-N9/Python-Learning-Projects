# 1. This is a comment symbol #.

                                #_______________________________________________________________

# 2. '' or "" => Strings can be in single or double quotes. It is important to them consistent.

                                #_______________________________________________________________
                                
# 3. Variable: 
    # Store data that can be a a number, a string, a Boolean, a list or some other data type
    # Needs to define variable 
    # An underscore character 
    # Can't start with a number
        
sport = "golf"
wild_animal = "lion" # This variable has underscore.

                                #_______________________________________________________________
                                
# 4. print() function outputs text to screen/terminal. 

print("Hello World!") # Hello World

favirote_color = "green"

print("My favirote color is " + favirote_color + ".") # My favirote color is green

# f-strings are string literals. Curly braces enclose the expressions, which can be variables or more complex expressions, so in this case, a variable.
# This is more preferred since it is clean and easier to read.
print(f"{wild_animal}") # lion
print(f"My favirote color is {favirote_color}.") # My favirote color is green. 

                                #_______________________________________________________________

# 5. Numbers

an_int = 2 # integer or int is a whole number
a_float = 2.15 # floating-point number or a float uses decimal number
                              
                                #_______________________________________________________________

# 6. Calculations with Arithmetic Operations -- converts all ints to floats before performing division

print(573 - 74 + 1) # 500

print(25 * 2) # 50

print(10 / 5) # 2.0

                                #_______________________________________________________________

# 7. Exponents: operation notation is to use **

print(2 ** 10) # 2 to the 10th power, or 1024

print(8 ** 2) # 8 squared, or 64

print(9 ** 3) # 9 * 9 * 9, 9 cubed, or 729

print(4 ** 0.5) # 4 to the half power, or 2

                                #_______________________________________________________________

# 8. Modulo

print(29 % 5) # Prints 4 because 29 / 5 is 5 with a remainder of 4
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
print(44 % 2) # Prints 0

# Number 3 is the divisor. The result of the first modulo operation is 0. As the dividend increases by 1, the remainder increases by 1 until we reach the following number evenly divisible by 3. This creates a pattern that repeats continuously as the dividend increases by 1.
print(3 % 3) # Prints 0
print(4 % 3) # Prints 1
print(5 % 3) # Prints 2
print(6 % 3) # Prints 0
print(7 % 3) # Prints 1

                                #_______________________________________________________________
                                
# 9. Concatenation: It can add two or more strings

greeting_text = "Hey there!"
question_text = "How are you doing?"

full_text = greeting_text + " " + question_text

print(full_text) # Hey there! How are you doing?

                                #_______________________________________________________________

# 10. Plus Equals: When you have a number saved in a variable and want to add to the current value of the variable, you can use the += operator (plus-equals)

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers # 50.00

nice_sweater = 39.00
fun_books = 20.00

# Update total_price:
total_price += nice_sweater # 50.00 + 39.00 = 89.00
total_price += fun_books # 89.00 + 20.00 = 109.00

print("The total price is", total_price)  # The total price is 109.0

# Plus-equals operator also can be used for string concatenation
write_note = "Don't forget to write notes!"

write_note += " Thank you!"

print(write_note) # Don't forget to write notes! Thank you!

                                #_______________________________________________________________

# 11. Multi-line Strings: Creating a string that occupies multiple lines leads to SyntaxError. It is multi-line strings using three quote-marks (""" or '''). The string doesn't end until the next triple-quote.

to_you = """ 
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""

print(to_you) 





