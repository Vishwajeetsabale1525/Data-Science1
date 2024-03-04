# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:22:16 2023

@author: Vishwajeet
"""
# Define a function called make_pizza that accepts a 'size' parameter and any number of 'toppings' as variable positional arguments
def make_pizza(size, *toppings):
    # Print a message indicating the size of the pizza and the toppings being added
    print(f"\nMaking a {size} pizza with the following toppings:")
    # Iterate over each topping in the 'toppings' tuple
    for topping in toppings:
        # Print each topping with a dash before it
        print(f"- {topping}")

# Call the make_pizza function with a 16-inch pizza size and 'Peprani' topping
make_pizza(16, 'Peprani')
# Call the make_pizza function with a 12-inch pizza size and multiple toppings ('mashroom', 'green_papers', 'extra chess')
make_pizza(12, 'mashroom', 'green_papers', 'extra chess')

# Import the 'pizza' module
import pizza

# Call the make_pizza function from the 'pizza' module with a 16-inch pizza size and 'Peprani' topping
pizza.make_pizza(16, 'Peprani')
# Call the make_pizza function from the 'pizza' module with a 12-inch pizza size and multiple toppings ('mashroom', 'green_papers', 'extra chess')
pizza.make_pizza(12, 'mashroom', 'green_papers', 'extra chess')
