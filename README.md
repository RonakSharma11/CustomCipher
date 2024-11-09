# CustomCipher
## Hill Cipher Implementation

This repository contains an implementation of the Hill cipher, a classical encryption algorithm that utilizes linear algebra concepts for encrypting and decrypting messages. The code demonstrates how to use a key matrix for encryption and decryption, along with proper handling of padding to ensure the integrity of the original message.

## Features

- **Encryption and Decryption**: Encrypt plaintext messages using a key matrix and decrypt them back to their original form.
- **Dynamic Key Matrix**: The key matrix can be generated randomly, ensuring that each encryption session can use a different key.
- **Padding Handling**: Automatically pads plaintext to ensure even-length blocks for encryption and removes padding during decryption.
- **Modular Arithmetic**: Uses modulo operations to ensure all calculations remain within the bounds of the alphabet (A-Z).

## How It Works

1. **Input Plaintext**: The user is prompted to enter a plaintext message consisting of letters only.
2. **Key Matrix Generation**: A key matrix is generated or imported, which is used for both encryption and decryption.
3. **Encryption Process**:
   - The plaintext is converted into numerical values based on their position in the alphabet (A=0, B=1, ..., Z=25).
   - If the plaintext length is odd, it is padded with 'A' (0) to make it even.
   - The plaintext is divided into blocks and encrypted using the key matrix.
4. **Decryption Process**:
   - The ciphertext is decrypted using the inverse of the key matrix.
   - If padding was added during encryption, it is removed from the decrypted output.

## Usage

To run the Hill cipher implementation:

1. Clone this repository:
   ```bash
   git clone https://github.com/RonakSharma11/CustomCipher.git
   cd HillCipher
Ensure you have Python installed along with the required libraries (numpy).

Run the main script:
  ```bash
  python HillCipher.py
  ```

## Example
  ```bash
  Generated Matrix:
 [[-15 -14]
 [-14 -13]]
Inverse Matrix:
 [[-13  14]
 [ 14 -15]]
Determinant: -1
Using Key Matrix (K):
 [[-15 -14]
 [-14 -13]]
Enter a message to encrypt (letters only): plsgetthisright
Plaintext as Matrix:
[[15]
 [11]]
[[18]
 [ 6]]
[[ 4]
 [19]]
[[19]
 [ 7]]
[[ 8]
 [18]]
[[17]
 [ 8]]
[[6]
 [7]]
[[19]
 [ 0]]
Plaintext: plsgetthisright
Encrypted: LLKIMJHHSSXWUHBU
Using Inverse Key Matrix (K^-1):
 [[13 12]
 [12 15]]
Decrypted: PLSGETTHISRIGHT
```

## Security Considerations 
While this implementation provides basic encryption capabilities, it is important to note that the Hill cipher has known vulnerabilities:
- **It can be susceptible to brute-force attacks if small matrices are used.**
- **Combining this method with other encryption techniques or using larger key matrices can improve security.**

## License 
This project is licensed under the MIT License - see the LICENSE file for details.
