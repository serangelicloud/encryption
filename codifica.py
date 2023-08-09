import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class Crypt:

    @staticmethod
    def encrypt(word, key):
        salt = os.urandom(16)
        iv = os.urandom(16)

        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=10000,
        salt=salt,
        length=23,  # Use 32 bytes (256 bits) key size
        backend=default_backend())

        key = base64.urlsafe_b64encode(kdf.derive(key.encode()))
        cipher = Cipher(
            algorithms.AES(key),
            modes.CFB(iv),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(word.encode()) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        combined_data = salt + iv + encrypted_data
        return base64.b64encode(combined_data).decode()

    @staticmethod
    def decrypt(encrypted_word, key):
        combined_data = base64.b64decode(encrypted_word)

        salt = combined_data[:16]
        iv = combined_data[16:32]
        encrypted_data = combined_data[32:]

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=10000,
            salt=salt,
            length=23,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(key.encode()))
        cipher = Cipher(
            algorithms.AES(key),
            modes.CFB(iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()

        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

        return unpadded_data.decode()


### UTILITIES FOR IMPORT ###


# PRINT ENCRYPTED WORD

# word = ("ARandomSentence") 
# key = ("key") ## key has to be a string not a integer
# encrypted_word = crypter.Crypt.encrypt(word, key)
# print(encrypted_word)

# PRINT DECRYPTED WORD

# key = ("5703008")
# decrypted_word = crypter.Crypt.decrypt(encrypted_word, key)
# print("Decrypted word:", decrypted_word)

# FOR ERROR HANDLING 

    # try:
    #     word = "ARandomSentence"
    #     key = "key"

    #     # Encrypt the password
    #     encrypted_word = Crypt.encrypt(word, key)
    #     print("Encrypted word:", encrypted_word)

    #     # Decrypt the password
    #     decrypted_word = Crypt.decrypt(encrypted_word, key)
    #     print("Decrypted word:", decrypted_word)
    # except Exception as e:
    #     print(e)