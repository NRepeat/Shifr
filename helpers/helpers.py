def perform_cipher(method, text, shift,key):
    if key:
        return method['cipher'](text,key)
    if shift == 0:
        return method['cipher'](text)
    else:
        return method['cipher'](text, shift)
def perform_decipher(method, text, shift,key):
    if key:
        return method['decipher'](text,key)
    if shift == 0:
        return method['decipher'](text)
    else:
        return method['decipher'](text, shift)  
def choose_method(input_value):
    while True:
        if input_value == 6:
            return perform_cipher
        method = input("Choose action. 1: Cipher, 2: Decipher\n")
        if method == '1':
            return perform_cipher
        elif method == '2':
            return perform_decipher
        else:
            print("Invalid choice. Please choose 1 for Cipher or 2 for Decipher.")