# created list of menu items
menu = ['Tea', 'Coffee', 'Sandwich', 'Cake']

# created dictionaries to store stock and price values
stock = {'Tea': 500,
        'Coffee': 500,
        'Sandwich': 35,
        'Cake': 30}

price = {'Tea': 1.80,
        'Coffee': 2.95,
        'Sandwich': 3.99,
        'Cake': 4.50}

# looped through the menu to store the calculation of the total stock and printed the value
total_stock = 0
for i in menu:
    total_stock += stock[i] * price[i]
print(f"The total stock value is: £{total_stock}")
