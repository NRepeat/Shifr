def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    matrix = []
    used_chars = set()

    for char in key.upper():
        if char not in used_chars and char != 'J':
            matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, matrix_char in enumerate(row):
            if matrix_char == char:
                return i, j
    return None

def encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = text.upper().replace('J', 'I')
    result = ''
    i = 0

    while i < len(text):
        char1 = text[i]
        char2 = text[i+1] if i+1 < len(text) else 'X'
        if char1 == char2:
            char2 = 'X'

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
        
        i += 2

    return result

def decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    result = ''
    i = 0

    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
        
        i += 2

    return result


