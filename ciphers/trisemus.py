def cipher(text, key):
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    matrix = ''
    for char in key.upper():
        if char not in matrix:
            matrix += char
    for char in alphabet:
        if char not in matrix:
            matrix += char
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    def get_position(char):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return None

    result = ""
    for char in text.upper():
        if char == 'J':
            char = 'I'
        pos = get_position(char)
        if pos:
            result += matrix[(pos[0] + 1) % 5][pos[1]]
        else:
            result += char
    return result

def decipher(text, key):
   
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    matrix = ''
    for char in key.upper():
        if char not in matrix:
            matrix += char
    for char in alphabet:
        if char not in matrix:
            matrix += char
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    def get_position(char):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return None

    result = ""
    for char in text.upper():
        if char == 'J':
            char = 'I'
        pos = get_position(char)
        if pos:
            result += matrix[(pos[0] - 1) % 5][pos[1]]
        else:
            result += char
    return result
