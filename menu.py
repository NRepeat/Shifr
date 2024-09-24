from data.data import ciphers_names
from data.data import menu_case
from helpers.helpers import choose_method


def interface():
    for name in ciphers_names:
        print(name)
    input_value = int(input('Choose encryption method: ').strip()) - 1 

    
    method = choose_method(input_value)
    text = input('Enter text: ')
    key = ''
    shift = 0
    if input_value == 0:
            shift = int(input('Enter shift (for Caesar cipher): '))
            
    elif input_value == 2 or input_value == 3 or input_value == 6:
            key = input('Enter key: ')
    else:
            shift = 0  
            key = ''
    
    cipher = menu_case[input_value]
    
    print(f"Resulting text: {method(cipher,text, shift,key)}")



