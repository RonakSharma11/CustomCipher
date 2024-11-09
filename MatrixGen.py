import numpy as np

# Global variables to hold the generated matrix and its inverse
matrix = None
inverse_matrix = None

def generate_integer_inverse_matrix():
    global matrix, inverse_matrix  # Use the global variables
    while True:
        # Generate random integer entries for a 2x2 matrix in the range -20 to 20
        a, b, c, d = np.random.randint(-20, 21, 4)
        matrix_candidate = np.array([[a, b], [c, d]])

        # Calculate the determinant
        det = a * d - b * c

        # Check if the determinant is ±1
        if abs(det) == 1:
            inverse_matrix = np.array([[d, -b], [-c, a]])
            print("Generated Matrix:\n", matrix_candidate)
            print("Inverse Matrix:\n", inverse_matrix)
            print("Determinant:", det)
            matrix = matrix_candidate  # Store the generated matrix
            return matrix, inverse_matrix

# Generate a matrix with an integer-only inverse
generate_integer_inverse_matrix()