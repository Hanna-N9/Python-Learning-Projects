# This program uses class to keep things organized in the restaurant 'Basta Fazoolin’ with My Heart.'

# Making the Menus -- four different menus: brunch, early-bird, dinner, and kids.

# Create a Menu class
# Give Menu a constructor with the five parameters self, name, items, start_time, and end_time
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

# "Add a method to the Menu class that returns a __repr__ representation of the menu, including its name and availability hours."
  def __repr__(self):
      return f"{self.name} menu available from {self.start_time} to {self.end_time}"

# Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch
# Let’s create our second menu item early_bird. This second menu is served from 3pm to 6pm. The following items are sold during early_bird
# Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:
# Let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.

# Create the brunch menu
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 
    'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 
    'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch_items, '11am', '4pm')

# Create the early bird menu
early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}
early_bird_menu = Menu('Early Bird', early_bird_items, '3pm', '6pm')

# Create the dinner menu
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}
dinner_menu = Menu('Dinner', dinner_items, '5pm', '11pm')

# Create the kids menu
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
}
kids_menu = Menu('Kids', kids_items, '11am', '9pm')

print(brunch_menu)
print(early_bird_menu)
print(dinner_menu)
print(kids_menu)
