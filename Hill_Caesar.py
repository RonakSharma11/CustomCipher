import numpy as np


def text_to_numbers(text):
    """Convert text to numbers (A=0, B=1, ..., Z=25)."""
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]


def numbers_to_text(numbers):
    """Convert numbers back to text (0=A, 1=B, ..., 25=Z)."""
    return ''.join(chr(num + ord('A')) for num in numbers)


def mod_26(matrix):
    """Apply modulo 26 to each element of the matrix."""
    return np.mod(matrix, 26)


def caesar_encrypt(text, shift):
    """Encrypt text using Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A')
            result += chr((ord(char.upper()) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    """Decrypt text using Caesar cipher."""
    return caesar_encrypt(text, -shift)


def encrypt(plaintext, key_matrix):
    """Encrypt the plaintext using the Hill cipher."""
    plaintext_numbers = text_to_numbers(plaintext)

    original_length = len(plaintext_numbers)
    if original_length % 2 != 0:
        plaintext_numbers.append(0)  # Padding with 'A' (0)

    ciphertext_numbers = []

    for i in range(0, len(plaintext_numbers), 2):
        plain_matrix = np.array([[plaintext_numbers[i]], [plaintext_numbers[i + 1]]])
        encrypted_matrix = mod_26(np.dot(key_matrix, plain_matrix))
        ciphertext_numbers.extend(encrypted_matrix.flatten().tolist())

    ciphertext = numbers_to_text(ciphertext_numbers)

    return ciphertext, ciphertext_numbers, original_length


def decrypt(ciphertext_numbers, key_matrix, original_length):
    """Decrypt the ciphertext using the inverse of the key matrix."""

    det = int(np.round(np.linalg.det(key_matrix)))  # Determinant of K
    inv_det = pow(det, -1, 26)  # Modular multiplicative inverse of determinant

    adjugate_matrix = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                                [-key_matrix[1][0], key_matrix[0][0]]])

    inverse_key_matrix = mod_26(inv_det * adjugate_matrix)

    # Displaying matrices
    print("Using Key Matrix (K):")
    print(key_matrix)

    print("Using Inverse Key Matrix (K^-1):")
    print(inverse_key_matrix)

    decrypted_numbers = []

    for i in range(0, len(ciphertext_numbers), 2):
        cipher_matrix = np.array([[ciphertext_numbers[i]], [ciphertext_numbers[i + 1]]])
        decrypted_matrix = mod_26(np.dot(inverse_key_matrix, cipher_matrix))
        decrypted_numbers.extend(decrypted_matrix.flatten().tolist())

    decrypted_text = numbers_to_text(decrypted_numbers)

    if len(decrypted_text) > original_length:
        decrypted_text = decrypted_text[:-1]  # Remove padding 'A'

    return decrypted_text


# Example usage
if __name__ == "__main__":
    # Define a key matrix for Hill cipher
    matrix = np.array([[-5, 19], [-1, 4]])

    # Get user input
    plaintext = input("Enter a message to encrypt (letters only): ")

    # Step 1: Encrypt with Caesar Cipher first
    shift_value = int(input("Enter shift value for Caesar Cipher: "))

    caesar_encrypted_text = caesar_encrypt(plaintext, shift_value)

    print(f"Caesar Encrypted Text: {caesar_encrypted_text}")

    # Step 2: Encrypt with Hill Cipher
    hill_encrypted_message, ciphertext_numbers, original_length = encrypt(caesar_encrypted_text, matrix)

    print(f"Hill Encrypted Text: {hill_encrypted_message}")

    # Step 3: Decrypt with Hill Cipher
    hill_decrypted_message = decrypt(ciphertext_numbers, matrix, original_length)

    # Step 4: Decrypt with Caesar Cipher
    final_decrypted_message = caesar_decrypt(hill_decrypted_message, shift_value)

    print(f"Final Decrypted Text: {final_decrypted_message}")