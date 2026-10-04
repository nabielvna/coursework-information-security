from utils import generate_random_key
from crypto import encrypt, decrypt

def print_menu():
    print("\n=== DES ENCRYPTION AND DECRYPTION PROGRAM ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("==========================================")

def get_user_input():
    while True:
        try:
            choice = int(input("Choose menu (1-3): "))
            if 1 <= choice <= 3:
                return choice
            print("Invalid choice. Please choose 1-3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def encrypt_text():
    plaintext = input("\nEnter text to encrypt: ")
    key = generate_random_key()
    print("\nKey used:", key)
    
    try:
        ciphertext = encrypt(plaintext, key)
        print("\nEncryption Result:")
        print("Plaintext:", plaintext)
        print("Ciphertext:", ciphertext)
        print("\nSave this key for decryption:", key)
    except Exception as e:
        print("\nError during encryption:", str(e))

def decrypt_text():
    ciphertext = input("\nEnter encrypted text: ")
    key = input("Enter key: ")
    
    try:
        decrypted_text = decrypt(ciphertext, key)
        print("\nDecryption Result:")
        print("Decrypted text:", decrypted_text)
    except Exception as e:
        print("\nError during decryption:", str(e))
        print("Make sure the encrypted text and key are correct.")

def main():
    while True:
        print_menu()
        choice = get_user_input()
        
        if choice == 1:
            encrypt_text()
        elif choice == 2:
            decrypt_text()
        else:
            print("\nThank you for using this program!")
            break

if __name__ == "__main__":
    main()