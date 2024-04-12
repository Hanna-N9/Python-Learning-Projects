# This program uses functions to help physics teacher's students calculate some fundamental physical properties.

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Turn up the Temperature

# Convert Fahrenheit to Celsiu
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp 

f100_in_celsius = f_to_c(100)

# Convert Celsiu to Fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

# Use the Force

# Return mass multiplied by acceleration
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print(f"The GE train supplies {train_force} Newtons of force.")

# c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.
# get_energy should return mass multiplied by c squared
def get_energy(mass, c = 3*10**8):
    return mass * c**2

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# Do the Work

# Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")


