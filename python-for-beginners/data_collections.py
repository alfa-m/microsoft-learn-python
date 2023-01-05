# Collections of data (25-26)

# Arrays - Unordered, numerical data, numerical index
from array import array

grades = array('d',[9.85, 8.0])
grades.append(9.0)
print(grades, type(grades))
print(grades[1])
print()

# Dictionaries - Unordered, any type of data, key index
shampoo = {
    'brand': 'Dove',
    'price': 15.00
}
print(shampoo, type(shampoo))

moisturizer = {}
moisturizer['brand'] = 'The Body Shop'
moisturizer['price'] = 40.00
print(moisturizer, type(moisturizer))

print(moisturizer['brand'])
print()

# Lists - Unordered, any type of data, numerical index
prices = []
prices.append(shampoo)
prices.append(moisturizer)
print(prices, type(prices))
print(prices[1])
print(prices[1]['brand'])
