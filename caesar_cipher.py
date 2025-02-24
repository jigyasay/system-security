def caesar_cipher(text, key, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        key = -key  
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char  #for spaces
    return result

def main():
    while True:
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter the message to encrypt: ")
            key= int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher(text, key, mode='encrypt')
            print("Encrypted message:", encrypted_text)
        
        elif choice == '2':
            text = input("Enter the message to decrypt: ")
            key= int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher(text, key, mode='decrypt')
            print("Decrypted message:", decrypted_text)
        
        elif choice == '3':
            print("Exiting the program")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()