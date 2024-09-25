def create_magic_square_3x3():
    return [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

def create_magic_square_4x4():
    return [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]

def encrypt(text, square):
    text = text.replace(" ", "")
    size = len(square)
    if len(text) < size ** 2:
        text += ' ' * (size ** 2 - len(text))

    encrypted = [''] * (size ** 2)
    for i in range(size):
        for j in range(size):
            encrypted[square[i][j] - 1] = text[i * size + j]

    return ''.join(encrypted)

def decrypt(cipher_text, square):
    size = len(square)
    decrypted = [''] * (size ** 2)
    for i in range(size):
        for j in range(size):
            decrypted[i * size + j] = cipher_text[square[i][j] - 1]
    
    return ''.join(decrypted).strip()


