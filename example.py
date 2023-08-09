from codifica import Crypt  # Import the Crypt class from the crypt module

def main():
    try:
        # Encrypting Data
        word = "ARandomSentence"
        key = "99"  # Replace with your encryption key

        encrypted_word = Crypt.encrypt(word, key)
        print("Encrypted word:", encrypted_word)

        # Decrypting Data
        encrypted_data = "FBE8501niABdhn3qnBHhjJJSQTwVu7qdZPyqboTsgZ0HYpcbWHkEfMyxft9luYih"  # Replace with your encrypted data
        decryption_key = "99"  # Replace with your encryption key

        decrypted_word = Crypt.decrypt(encrypted_data, decryption_key)
        print("Decrypted word:", decrypted_word)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
