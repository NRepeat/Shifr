def perform_cipher(method, text, shift,key):
    print(key)
    if key:
        return method['cipher'](text,key)
    if shift == 0:
        return method['cipher'](text)
    else:
        return method['cipher'](text, shift)
def perform_decipher(method, text, shift,key):
    print(key)
    if key:
        return method['decipher'](text,key)
    if shift == 0:
        return method['decipher'](text)
    else:
        return method['decipher'](text, shift)  
def choose_method(input_value):
    while True:
        method = input_value
        if method == True:
            return perform_cipher
        elif method == False:
            return perform_decipher
     