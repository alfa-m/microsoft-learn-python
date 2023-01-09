# Decorators (42-43)

## Creates a decorator
def pretty(func):
    def bubble():
        print('Begin of the wrapper')
        print('Calling your function')
        func()
        print('End of the wrapper')
    return bubble

## Calls the decorator
@pretty
def hello_message():
    print('Hello, how are you?')

## Calls the function that will be 'decorated'
hello_message()
