def caesar_cipher(text, shift, mode):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            if char.islower():
                # Shift within lowercase range (97-122 in ASCII)
                encrypted_char = chr((ord(char) - 97 + shift * mode) % 26 + 97)
            else:
                # Shift within uppercase range (65-90 in ASCII)
                encrypted_char = chr((ord(char) - 65 + shift * mode) % 26 + 65)
        else:
            encrypted_char = char  # Non-alphabetical characters remain unchanged
        
        encrypted_text += encrypted_char

    return encrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
        
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        
        message = input("Enter your message: ").strip()
        shift = int(input("Enter the shift value (a positive integer): "))
        
        if choice == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, 1)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'decrypt':
            decrypted_message = caesar_cipher(message, shift, -1)
            print(f"Decrypted message: {decrypted_message}")
        
        another = input("Do you want to encrypt/decrypt another message? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
