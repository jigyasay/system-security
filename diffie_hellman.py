def generate_public_key(base,private_key,prime):
    return pow(base,private_key,prime)
def generate_shared_secret(public_key,private_key,prime):
    return pow(public_key,private_key,prime)

def encrypt(message,key):
    encrypted =""
    for char in message:
        encrypted += chr(ord(char) ^ key)
    return encrypted

def decrypt(encrypted_message,key):
    return encrypt(encrypted_message,key)

def main():
    print("diffie hellman key exchange")
    P = int(input("enter a prime number"))
    G = int(input("enter a base number G"))

    alice_private = int(input("enter alice's private key"))
    alice_public = generate_public_key(G,alice_private,P)
    print("alice public key",alice_public)

    bob_private = int(input("enter bob's private key"))
    bob_public = generate_public_key(G,bob_private,P)
    print("bob's public key",bob_public)

    alice_shared = generate_shared_secret(bob_public,alice_private,P)
    bob_shared = generate_shared_secret(alice_public,bob_private,P)

    print("alice's shared secret key",alice_shared)
    print("bob's shared secret key",bob_shared)

    if alice_shared != bob_shared:
        print("error: check your inputs")
        return
    
    message = input("enter a message")
    encrypted = encrypt(message,alice_shared)
    print("encrypted msg : ",encrypted)

    decrypted = decrypt(encrypted,bob_shared)
    print("decrypted msg",decrypted)

if __name__ == "__main__":
    main()
