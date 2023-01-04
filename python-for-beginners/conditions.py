# Conditional structures (19-24)

## If
tax_fish = 0
price_fish = float(input('How much is the fish? '))

if price_fish >= 1.00:
    tax_fish = 0.07

final_price_fish = (1 + tax_fish) * price_fish

print('Tax rate: ', tax_fish)
print('Final price of the fish: ', final_price_fish)

## If-else
price_purchase = float(input('How much is the purchase? '))

if price_purchase >= 1.00:
    tax_purchase = 0.07
else:
    tax_purchase = 0

final_price_purchase = (1 + tax_purchase) * price_purchase

print('Tax rate: ', tax_purchase)
print('Final price of the purchase: ', final_price_purchase)

## If-elif
province = input('Where are you from? ')

if province.capitalize() == 'Alberta':
    province_tax = 0.05
elif province.capitalize() == 'Yukon':
    province_tax = 0.05
elif province.capitalize() == 'Ontario':
    province_tax = 0.13

print('Tax rate: ', province_tax)

## If-elif-else
province = input('Where are you from? ')

if province.capitalize() == 'Alberta':
    province_tax = 0.05
elif province.capitalize() == 'Yukon':
    province_tax = 0.05
elif province.capitalize() == 'Ontario':
    province_tax = 0.13
else:
    province_tax = 0.15

print('Tax rate: ', province_tax)

### OR condition
province = input('Where are you from? ')

if province.capitalize() == 'Alberta' or province.capitalize() == 'Yukon':
    province_tax = 0.05
elif province.capitalize() == 'Ontario':
    province_tax = 0.13
else:
    province_tax = 0.15

print('Tax rate: ', province_tax)

### Check a list of conditions
province = input('Where are you from? ')

if province in ('Alberta', 'Yukon', 'Nunavut'):
    province_tax = 0.05
elif province.capitalize() == 'Ontario':
    province_tax = 0.13
else:
    province_tax = 0.15

print('Tax rate: ', province_tax)

### Nested condition
home_country = input('Where did you come from? ')
price_poutine = float(input('How much is the poutine? '))

if home_country.lower() == 'canada':   
    if price_poutine >= 5.00:
        tax_poutine = 0.05
    else:
        tax_poutine = 0.02
else:
    print('You cannot buy poutine')

final_price_poutine = (1 + tax_poutine) * price_poutine

print('Tax rate: ', tax_poutine)
print('Final price of the fish: ', final_price_poutine)

### AND condition
home_country = input('Where did you come from? ')
price_poutine = float(input('How much is the poutine? '))

if home_country.lower() == 'canada' and price_poutine >= 5.00:
    tax_poutine = 0.05
else:
    print('You cannot buy poutine')

final_price_poutine = (1 + tax_poutine) * price_poutine

print('Tax rate: ', tax_poutine)
print('Final price of the fish: ', final_price_poutine)
