# Modules, packages and virtual environments (33-35) 
## Auxiliar file 2

### This example uses an package installed inside a virtual environment called 'venv'
### python -m venv venv
### ./venv/Scripts/activate.bat
### pip install -r requirements.txt

from colorama import init, Fore

def display_4(message_without_color = 'Boring message', is_boring = True):
    if is_boring:
        print('This is a boring message!')
    print(message_without_color)
    print()

def display_5(message_with_color = 'Template message', is_dope = True):
    if is_dope:
        print(Fore.CYAN + message_with_color)
    else:
        print(Fore.WHITE + message_with_color)
    print()