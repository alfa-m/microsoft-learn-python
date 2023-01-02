# Numbers (13-14)

## Alocanting a number to a variable
pi = 3.14159
print(pi)

## Turning input into a number ('cause every input is treated as a string)
first_number = input('Please, enter a number: ')
print(first_number)
second_number = input('Please, enter another number: ')
print(second_number)
print('Sum is:')

## Without type coercion, the inputs are concatened
print(first_number + second_number)

## With type coercion, the sum goes as expected
print(int(first_number) + int(second_number))
print(float(first_number) + float(second_number))

## Turning number into a string
day = 30
print('My birthday is on November ' + str(day))
