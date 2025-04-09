import random
from sympy import isprime

def gen_prime(bits=8):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num
        
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def mod_inverse(e,phi):
    for d in range(2,phi):
        if(d*e)% phi==1:
            return d
    return None

def gen_keys(bits=8):
    p=gen_prime(bits)
    q=gen_prime(bits)

    if p==q:
        q=gen_prime(bits)
    
    n=p*q
    phi=(p-1)*(q-1)

    e=random.randrange(2,phi) #public key
    while gcd(e,phi)!=1:
        e=random.randrange(2,phi)

    d=mod_inverse(e,phi) #private key

    return((e,n),(d,n))

def encrypt(plain_text,public_key):
    e,n = public_key
    cipher_text = [pow(ord(char),e,n) for char in plain_text]
    return cipher_text

def decrypt(cipher_text,private_key):
    d,n = private_key
    plain_text = ''.join(chr(pow(char,d,n)) for char in cipher_text)
    return plain_text

public_key,private_key = gen_keys(bits=8)
message = input("enter the message")

cipher = encrypt(message,public_key)
decrypted = decrypt(cipher,private_key)

print("public key",public_key)
print("private key",private_key)
print("original msg",message)
print("encrypted msg",cipher)
print("decrypted msg",decrypted)


