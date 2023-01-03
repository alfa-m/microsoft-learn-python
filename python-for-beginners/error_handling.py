# Error handling (17-18)

# For handling errors that you wish to log or gracefully exit, use 'try except finally'
x = 23
y = 2

# try some code
try:
    division = x / y

# if determined error occur, do this
except ZeroDivisionError as e:
    print('Cannot divide by zero')

# if not, do this
else:
    print(division)

# show this anyway
finally:
    print('Exiting the code')
