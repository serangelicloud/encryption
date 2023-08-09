# Cryptography Utility with AES Encryption

This Python script provides a `Crypt` class that allows you to perform AES encryption and decryption using PBKDF2-based key derivation. It employs the `cryptography` library to ensure secure and efficient encryption and decryption of sensitive data.

## Features

- AES encryption and decryption with PBKDF2-based key derivation
- Randomly generated salt and IV (Initialization Vector) for increased security
- Padding to ensure that the data being encrypted or decrypted is a multiple of the block size

## Requirements

- Python 3.x
- `cryptography` library (Install using `pip install cryptography`)

## Usage

### Encrypting Data

To encrypt data using the `Crypt` class, follow these steps:

1. Import the `Crypt` class from the script.
2. Initialize the `Crypt` class.
3. Use the `encrypt` method to encrypt the data.

```python
from crypt import Crypt

word = "ARandomSentence"
key = "your_key"  # Replace with your encryption key

encrypted_word = Crypt.encrypt(word, key)
print("Encrypted word:", encrypted_word)
```

### Decrypting Data
To decrypt data using the Crypt class, follow these steps:

1. Import the Crypt class from the script.
2. Initialize the Crypt class.
3. Use the decrypt method to decrypt the data.

```python
from crypt import Crypt

encrypted_word = "your_encrypted_word"  # Replace with your encrypted data
key = "your_key"  # Replace with your encryption key

decrypted_word = Crypt.decrypt(encrypted_word, key)
print("Decrypted word:", decrypted_word)
```

### Example
For a complete example, refer to the provided example.py script.

## Utilities for Import
The script also includes utility functions for demonstrating the usage of the Crypt class. These utilities showcase how to encrypt and decrypt data, and how to handle exceptions.

To use the utilities, uncomment the desired section and replace the example values with your own.

## Error Handling
The script provides error handling examples within the utilities. When using the Crypt class, it's important to handle exceptions that may arise during encryption and decryption, such as incorrect keys or corrupted data.

## License
This script is provided under the MIT License. You are free to modify and use it for your own purposes.