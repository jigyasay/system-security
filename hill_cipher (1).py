import numpy as np

def mod_inverse(a, m):
    
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def inverse_matrix_2x2(matrix):
    
    det = int(np.round(np.linalg.det(matrix)))
    if np.gcd(det, 26) != 1:
        raise ValueError("Matrix is not invertible under modulo 26.")
    det_inv = mod_inverse(det, 26)
    adjugate = np.array([[matrix[1, 1], -matrix[0, 1]],
                         [-matrix[1, 0], matrix[0, 0]]])
    inverse = det_inv * adjugate
    inverse = np.remainder(inverse, 26)
    return inverse.astype(int)

def process_input(text):

    return ''.join([char for char in text if char.isalpha()])

def char_to_num(char):
    """Map a character to a number (0-25)."""
    if char.isupper():
        return ord(char) - ord('A')
    else:
        return ord(char) - ord('a')

def num_to_char(num, is_upper):
    """Map a number (0-25) back to a character, preserving case."""
    if is_upper:
        return chr(num + ord('A'))
    else:
        return chr(num + ord('a'))

def encrypt(plaintext, key_matrix):
    
    processed_text = process_input(plaintext)
    size = key_matrix.shape[0]
    padding_char = 'x'  # Using 'x' as the padding character
    if len(processed_text) % size != 0:
        processed_text += padding_char * (size - len(processed_text) % size)
    ciphertext = ''
    for i in range(0, len(processed_text), size):
        block = [char_to_num(char) for char in processed_text[i:i + size]]
        block = np.array(block).reshape(size, 1)
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join(num_to_char(num, processed_text[i + idx].isupper())
                              for idx, num in enumerate(encrypted_block.flatten()))
    return ciphertext

def decrypt(ciphertext, key_matrix):
   
    size = key_matrix.shape[0]
    inverse_key_matrix = inverse_matrix_2x2(key_matrix)
    plaintext = ''
    for i in range(0, len(ciphertext), size):
        block = [char_to_num(char) for char in ciphertext[i:i + size]]
        block = np.array(block).reshape(size, 1)
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        plaintext += ''.join(num_to_char(num, ciphertext[i + idx].isupper())
                             for idx, num in enumerate(decrypted_block.flatten()))
    return plaintext.rstrip('x')  # Remove trailing padding characters

def main():
    key_matrix = np.array([[2, 3],
                           [3, 6]])
    
    det = int(np.round(np.linalg.det(key_matrix)))
    if np.gcd(det, 26) != 1:
        print("Error: The key matrix is not invertible under modulo 26.")
        return

    plaintext = "Hello me"
    print(f"Plaintext: {plaintext}")

    ciphertext = encrypt(plaintext, key_matrix)
    print(f"Encrypted text: {ciphertext}")

    decrypted_text = decrypt(ciphertext, key_matrix)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
