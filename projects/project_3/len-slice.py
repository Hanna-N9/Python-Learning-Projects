# This program uses Python lists to organize some of sales data for a new pizza joint in the neighborhood.

# Make Some Pizzas

# To keep track of the kinds of pizzas you sell, create a list called toppings
topping = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# To keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of occurrences of 2 in the prices list, and store the result in a variable called num_two_dollar_slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices) # 3

# Find the length of the toppings list 
num_pizzas = len(topping)
print(num_pizzas) # 7

# Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas
print(f"We sell {num_pizzas} different kinds of pizza!") # We sell 7 different kinds of pizza!

# Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices
pizza_and_prices = [2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]

# Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices) # [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

# Sorting and Slicing Pizzas

# Sort pizza_and_prices
pizza_and_prices.sort()
print(pizza_and_prices) # [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [3, 'sausage'], [6, 'pineapple'], [7, 'anchovies']]

# Store the first element of pizza_and_prices
cheapest_pizza = pizza_and_prices[0]

# Get the last item of the pizza_and_prices list 
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since someone bought the last slice
pizza_and_prices.pop()

# Add a new topping called "peppers". Need to be after [2, "pepperoni"] but before [3, "sausage"] since the list is sorted in order
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices) # [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage'], [6, 'pineapple']]

# Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list
three_cheapest = pizza_and_prices[:3]
print(three_cheapest) # [[1, 'cheese'], [2, 'mushrooms'], [2, 'olives']]





