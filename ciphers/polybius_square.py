polybius_square = {
    'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
    'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 
    'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
    'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
    'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
}
def encrypt(text):
    return ''.join(polybius_square[char.upper()] for char in text if char.upper() in polybius_square)

def decrypt(code):
    reverse_square = {v: k for k, v in polybius_square.items()}
    return ''.join(reverse_square[code[i:i+2]] for i in range(0, len(code), 2))



