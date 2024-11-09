import numpy as np
from MatrixGen import matrix  # Importing the generated matrix from MatrixGen.py


def text_to_numbers(text):
    """Convert text to numbers (A=0, B=1, ..., Z=25)."""
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]


def numbers_to_text(numbers):
    """Convert numbers back to text (0=A, 1=B, ..., 25=Z)."""
    return ''.join(chr(num + ord('A')) for num in numbers)


def mod_26(matrix):
    """Apply modulo 26 to each element of the matrix."""
    return np.mod(matrix, 26)


def encrypt(plaintext, key_matrix):
    """Encrypt the plaintext using the Hill cipher."""
    # Convert plaintext to numbers
    plaintext_numbers = text_to_numbers(plaintext)

    # Ensure plaintext length is even
    original_length = len(plaintext_numbers)
    if original_length % 2 != 0:
        plaintext_numbers.append(0)  # Padding with 'A' (0)

    # Display the plaintext as a matrix
    print("Plaintext as Matrix:")
    for i in range(0, len(plaintext_numbers), 2):
        plain_matrix = np.array([[plaintext_numbers[i]], [plaintext_numbers[i + 1]]])
        print(plain_matrix)

    # Create 2x1 matrices and encrypt
    ciphertext_numbers = []

    for i in range(0, len(plaintext_numbers), 2):
        # Create a 2x1 matrix from the plaintext
        plain_matrix = np.array([[plaintext_numbers[i]], [plaintext_numbers[i + 1]]])

        # Multiply by the key matrix and apply mod 26
        encrypted_matrix = mod_26(np.dot(key_matrix, plain_matrix))

        # Append the result to ciphertext
        ciphertext_numbers.extend(encrypted_matrix.flatten().tolist())

    # Convert encrypted numbers back to text
    ciphertext = numbers_to_text(ciphertext_numbers)

    return ciphertext, ciphertext_numbers, original_length


def decrypt(ciphertext_numbers, key_matrix, original_length):
    """Decrypt the ciphertext using the inverse of the key matrix."""

    # Calculate the inverse of the key matrix modulo 26
    det = int(np.round(np.linalg.det(key_matrix)))  # Determinant of K
    inv_det = pow(det, -1, 26)  # Modular multiplicative inverse of determinant

    # Calculate adjugate matrix for inverse calculation
    adjugate_matrix = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                                [-key_matrix[1][0], key_matrix[0][0]]])

    inverse_key_matrix = mod_26(inv_det * adjugate_matrix)

    # Display the inverse key matrix being used for decryption
    print("Using Inverse Key Matrix (K^-1):\n", inverse_key_matrix)

    # Create a list to hold decrypted numbers
    decrypted_numbers = []

    for i in range(0, len(ciphertext_numbers), 2):
        # Create a 2x1 matrix from the ciphertext
        cipher_matrix = np.array([[ciphertext_numbers[i]], [ciphertext_numbers[i + 1]]])

        # Multiply by the inverse key matrix and apply mod 26
        decrypted_matrix = mod_26(np.dot(inverse_key_matrix, cipher_matrix))

        # Append the result to decrypted numbers
        decrypted_numbers.extend(decrypted_matrix.flatten().tolist())

    # Convert decrypted numbers back to text
    decrypted_text = numbers_to_text(decrypted_numbers)

    # Remove padding if necessary (if last character is 'A')
    if len(decrypted_text) > original_length:
        decrypted_text = decrypted_text[:-1]  # Remove padding 'A'

    return decrypted_text


if __name__ == "__main__":
    # Display the key matrix being used
    print("Using Key Matrix (K):\n", matrix)

    # Ask user for input plaintext message
    plaintext = input("Enter a message to encrypt (letters only): ")

    # Encrypt the message using the imported key matrix
    encrypted_message, ciphertext_numbers, original_length = encrypt(plaintext, matrix)

    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_message}")

    # Decrypting the message using the inverse of K
    decrypted_message = decrypt(ciphertext_numbers, matrix, original_length)

    print(f"Decrypted: {decrypted_message}")