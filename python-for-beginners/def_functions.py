# Defining functions (29-32)

# Function with no parameter
## Function that says hello
def say_hello():
    print('Hello, friend')

# Function with parameter
from datetime import datetime

## Function that shows the runtime of a task
def show_runtime(task_name = 'task completed'):
    print(task_name)
    print(datetime.now())
    print()

# Function returning a value
## Function that calculates the four basic math operations
def calculator(var_a = 0, var_b = 0):
    addition = var_a + var_b
    subtraction = var_a - var_b
    multiplication = var_a * var_b
    division = var_a / var_b

    calculations = [addition, subtraction, multiplication, division]

    return calculations

## Testing all functions
name = input('What is your name? ')
say_hello()
show_runtime()

first_variable = float(input('Enter the first number: '))
second_variable = float(input('Enter the second number: '))
results = calculator(var_a = first_variable, var_b = second_variable)
print(results)
show_runtime('Calculated the sum, subtraction, multiplication and division')
