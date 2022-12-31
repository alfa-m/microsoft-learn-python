# String manipulation

## Concatenating strings
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Hello', first_name, last_name)
print('Hello,' + first_name + last_name)
print('Hello,' + ' ' + first_name + ' ' + last_name)

## String functions
phrase = 'wrItInG LiKe gAmZeE'

### Transforming all letters to uppercase
print(phrase.upper())

### Transforming all letters to lowercase
print(phrase.lower())

### Capitalizing the first letter
print(phrase.capitalize())

### Counting the amount of pieces of string inside a string
print(phrase.lower().count('e'))

### Putting it all together
print('Hello,', first_name.capitalize(), last_name.capitalize())

## String formatting
### Basic formatting
print('Hello, {} {}'.format(first_name,last_name))

### Index formatting
print('Hello, {0} {1}'.format(first_name,last_name))

### Direct formatting (available only in python 3)
print(f'Hello, {first_name} {last_name}')
