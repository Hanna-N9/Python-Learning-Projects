# Build a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

  # Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
  # Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
  # Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

# Ground Shipping - how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table
weight = 5

if weight <= 2:
 cost = weight * 1.5 + 20
 print(cost)
elif 2 < weight <= 6:
 cost = weight * 3 + 20
 print(cost)
elif 6 < weight <= 10:
 cost = weight * 4 + 20
 print(cost)
elif weight > 10:
 cost = weight * 4.75 + 20
 print(cost)
  
# Ground Shipping Premium - Flat charge: $125.00 and not charged for weight
cost_ground_premium = 125.00
print(weight + cost_ground_premium )

# Drone Shipping
if weight <= 2:
  cost = weight * 4.50
  print(cost)
elif 2 < weight <= 6:
 cost = weight * 9
 print(cost)
elif 6 < weight <= 10:
 cost = weight * 12
 print(cost)
elif weight > 10:
 cost = weight * 14.25
 print(cost)



