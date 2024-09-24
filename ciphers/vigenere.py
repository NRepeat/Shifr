def cipher(text, key):
    key = key.upper()
    result = ""
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            result += chr((ord(char) + shift - 65) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def decipher(ciphertext, key):
    key = key.upper()
    result = ""
    key_index = 0

    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            result += chr((ord(char) - shift - 65) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

