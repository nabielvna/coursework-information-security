# DES (Data Encryption Standard) Implementation

This project implements the Data Encryption Standard (DES) encryption algorithm in Python. It provides a command-line interface for encrypting and decrypting text using the DES algorithm.

## Overview

The DES implementation consists of several Python modules that work together to provide encryption and decryption functionality:

- `main.py`: Contains the command-line interface and program entry point
- `crypto.py`: Implements the main encryption and decryption functions
- `des.py`: Contains the core DES algorithm implementation
- `des_tables.py`: Stores the standard DES lookup tables and permutation matrices
- `utils.py`: Provides utility functions for bit manipulation and data conversion

## Features

- Text encryption using DES algorithm
- Text decryption with provided key
- Random key generation
- Command-line interface
- UTF-8 text support
- Built-in padding mechanism
- Base64 encoded output

## Requirements

- Python 3.x
- No additional external dependencies required

## Installation

1. Clone or download all the project files
2. Ensure all files are in the same directory
3. Run `main.py` using Python 3

```bash
python main.py
```

## Usage

### Running the Program

The program provides a simple menu-driven interface with three options:

1. Encrypt
2. Decrypt
3. Exit

### Encryption

To encrypt a text:

1. Select option 1 from the menu
2. Enter the text you want to encrypt
3. The program will generate a random key
4. Save the key and encrypted text for later decryption

### Decryption

To decrypt a text:

1. Select option 2 from the menu
2. Enter the encrypted text
3. Enter the key used for encryption
4. The program will show the decrypted text

## Technical Details

### Project Structure

- `main.py`: Program entry point and user interface
- `crypto.py`: High-level encryption/decryption functions
- `des.py`: Core DES algorithm implementation
- `des_tables.py`: DES algorithm lookup tables
- `utils.py`: Utility functions for data manipulation

### Implementation Details

The implementation follows the standard DES algorithm specification:

1. Initial permutation (IP)
2. 16 rounds of:
   - Key schedule generation
   - Feistel network structure
   - Substitution boxes (S-boxes)
   - Permutation function
3. Final permutation (IP⁻¹)

Key features of the implementation:

- 64-bit block size
- 56-bit effective key length (64-bit input key with parity bits)
- 16 rounds of Feistel network
- Built-in padding for variable length input
- Base64 encoding for output

### Utility Functions

The `utils.py` module provides several important functions:

- `generate_random_key()`: Generates an 8-character random key
- `string_to_bit_array()`: Converts text to binary
- `bit_array_to_string()`: Converts binary back to text
- `pad()`: Implements PKCS#7-style padding
- `unpad()`: Removes padding after decryption

## Security Considerations

Please note:

1. This is an educational implementation and may not be suitable for production use
2. DES is considered deprecated for secure communications
3. For production systems, use modern encryption standards like AES
4. The key should be stored securely and never shared publicly

## Error Handling

The implementation includes basic error handling for:

- Invalid input validation
- Incorrect key length
- Invalid encrypted text format
- Padding errors
- UTF-8 encoding/decoding errors

## Acknowledgments

This implementation follows the original DES specification and includes standard DES tables and permutations as defined in the original algorithm documentation.
