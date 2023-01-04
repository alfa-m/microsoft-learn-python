# Conditional structures (19-24)

## If
tax_fish = 0
price_fish = float(input('How much is the fish? '))

if price_fish >= 1.00:
    tax_fish = 0.07

final_price_fish = (1 + tax_fish) * price_fish

print('Tax rate: ', tax_fish)
print('Final price of the fish: ', final_price_fish)
print()

## If-else
price_purchase = float(input('How much is the purchase? '))

if price_purchase >= 1.00:
    tax_purchase = 0.07
else:
    tax_purchase = 0

final_price_purchase = (1 + tax_purchase) * price_purchase

print('Tax rate: ', tax_purchase)
print('Final price of the purchase: ', final_price_purchase)
print()

## If-elif
ingredients = 'bread + meat + lettuce'
extra_flavor = input('Enter an extra flavor: ')

if extra_flavor.lower() == 'cheese':
    ingredients = ingredients + ' + cheese'
elif extra_flavor.lower() == 'bacon':
    ingredients = ingredients + ' + bacon'
elif extra_flavor.lower() == 'sausage':
    ingredients = ingredients + ' + sausage'
elif extra_flavor.lower() == 'ham':
    ingredients = ingredients + ' + ham'
elif extra_flavor.lower() == 'eggs':
    ingredients = ingredients + ' + eggs'

print(ingredients)
print()

## If-elif-else
color = input('Choose a color: ')

if color.lower() == 'blue':
    print(color.capitalize(), 'is a primary color')
elif color.lower() == 'red':
    print(color.capitalize(), 'is a primary color')
elif color.lower() == 'yellow':
    print(color.capitalize(), 'is a primary color')
else:
    print(color.capitalize(), 'is not a primary color')
print()

### OR condition
province = input('Where are you from? ')

if province.capitalize() == 'Alberta' or province.capitalize() == 'Yukon':
    province_tax = 0.05
elif province.capitalize() == 'Ontario':
    province_tax = 0.13
else:
    province_tax = 0.15

print('Tax rate: ', province_tax)
print()

### Check a list of conditions
fruit = input('What fruit do you want? ')

if fruit.lower() in ('pineapple',
                     'orange',
                     'strawberry',
                     'lemon'):
    message = 'Fruit available'
else:
    message = 'Fruit not available'

print(message)
print()

### Nested condition
home_country = input('Which country did you come from? ')

if home_country.lower() == 'canada':
    price_poutine = float(input('How much is the poutine? '))

    if price_poutine >= 7.00:
        tax_poutine = 0.05
    else:
        tax_poutine = 0.02

    final_price_poutine = (1 + tax_poutine) * price_poutine

    print('Tax rate: ', tax_poutine)
    print('Final price of the fish: ', final_price_poutine)
else:
    print('You cannot buy poutine')
print()

### AND condition
gpa = float(input('What is your GPA? '))
low_grade = float(input('What is your lowest score? '))

if gpa >= 8.5 and low_grade >= 7.0:
    print('Congratulations!')
else:
    print("Sorry, you'll have to try again")
print()

### Boolean variables
pilot = int(input('What is your age? '))

if pilot >= 16:
    can_drive = True
else:
    can_drive = False

if can_drive:
    print('Go drive!')
  