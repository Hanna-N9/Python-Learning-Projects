# This program is to 
# store names and prices of a furniture store’s catalog in variables
# then process the total price and item list of customers, printing them to the output terminal


## Adding In The Catalog

# Lovely Loveseat 
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

lovely_loveseat_price = 254.00

# Stylish Settee
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

stylish_settee_price = 180.50

# Luxurious Lamp
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

luxurious_lamp_price = 52.15

# Define the sales tax rate
sales_tax = .088 # 8.8%


## Our First Customer

# A running tally of customer's expenses. And for now, 0 since customer hasn't purchased anything yet
customer_one_total = 0

# Description of things customer is purchasing and for now empty string
customer_one_itemization = ""

# Purchase Lovely Loveseat
customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

# Purchase Luxurious Lamp
customer_one_total += luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

# Check out by calculating the sales tax
customer_one_tax = customer_one_total * sales_tax

# Add the sales tax to the customer's total cost
customer_one_total += customer_one_tax

# Print out the heading of items
print("Customer One Items:")
print(customer_one_itemization)

# Print out the heading of total cost
print("Customer One Total:")
print(customer_one_total)

 










