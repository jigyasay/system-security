import math

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1: #similar to 5x mod26  where x will come as 21 coz (5*21)%26 gives 1 
            return i
    return None

def affine_cipher(text, a, b, mode='encrypt'):
    result = ""
    m = 26  
    
    if mode == 'decrypt':
        a_inv = mod_inverse(a, m)
        if a_inv is None:
            print("Error")
            return ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr(((a * (ord(char) - base) + b) % m) + base)
            else: 
                result += chr(((a_inv * ((ord(char) - base) - b)) % m) + base)
        else:
            result += char  
    return result

def main():
    while True:
        print("\nAffine Cipher Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice in ('1', '2'):
            text = input("Enter the message: ")
            a = int(input("Enter the multiplicative key (a): "))
            b = int(input("Enter the additive key (b): "))
            mode = 'encrypt' if choice == '1' else 'decrypt'
            
            if math.gcd(a, 26) != 1:
                print("Error: 'a' must be coprime with 26.")
                continue
            
            result = affine_cipher(text, a, b, mode)
            print("Result:", result)
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
