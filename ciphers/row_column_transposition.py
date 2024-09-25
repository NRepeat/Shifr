def encrypt(text, key):
    key_len = len(key)
    padding_length = key_len - len(text) % key_len
    text += ' ' * padding_length

    rows = [text[i:i + key_len] for i in range(0, len(text), key_len)]

    sorted_key = sorted([(ch, i) for i, ch in enumerate(key)])
    transposed_text = ''.join([''.join(row[k[1]] for row in rows) for k in sorted_key])

    return transposed_text

def decrypt(cipher_text, key):
    key_len = len(key)
    num_rows = len(cipher_text) 

    sorted_key = sorted([(ch, i) for i, ch in enumerate(key)])
    columns = [cipher_text[i * num_rows:(i + 1) * num_rows] for i in range(key_len)]

    decrypted_text = ''.join([''.join(columns[k[1]][i] for k in sorted_key) for i in range(num_rows)])
    return decrypted_text.strip()


