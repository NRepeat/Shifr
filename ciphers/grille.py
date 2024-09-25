import numpy as np

def create_grille_key(n):
    grille = np.array([[1, 0, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1],
                       [0, 1, 0, 0]])
    return grille

def cipher(text, grille):
    n = len(grille)
    if len(text) < n * n:
        text += ' ' * (n * n - len(text))
    
    cipher_grid = [[''] * n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if grille[i][j] == 1:
                cipher_grid[i][j] = text[idx]
                idx += 1

    return ''.join([''.join(row) for row in cipher_grid])

def decrypt(cipher_text, grille):
    n = len(grille)
    decrypted = [''] * (n * n)
    idx = 0
    for i in range(n):
        for j in range(n):
            if grille[i][j] == 1:
                decrypted[idx] = cipher_text[i * n + j]
                idx += 1
    return ''.join(decrypted).strip()


