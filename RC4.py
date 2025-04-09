mod=256
s=[]
for i in range(0,256):
    s.append(i)
#print(s)
PT=input("enter the text")
k=input("enter the key\n")
size=len(k)
key=[]
for i in range(0,256):
    base=ord(k[i%size])
    key.append(base)
#print(key)
#pseudo random generation ->new s array
j=0
for i in range(0,256):
    j=(j+s[i]+key[i])%mod
    s[i],s[j]=s[j],s[i]

#key scheduling -> genrating key stream
i=0
j=0
keystr=[]
for i  in range(1,len(PT)+1):
    j=(j+s[i])%mod
    s[i],s[j]=s[j],s[i]
    t=(s[i]+s[j])%mod
    keystr.append(s[t])

#encryption
plain_text=[]
for char in(PT):
    base=ord(char)
    plain_text.append(base)
i=0
CT=[]
for i in range(0,len(PT)):
    CT.append(plain_text[i] ^ keystr[i])
#print(CT)

C_T=""
for i in range(0,len(CT)):
    char=chr(CT[i])
    C_T += char
print(C_T)

#decryption
p_text=[]
for i in range(0,len(CT)):
    p_text.append(CT[i] ^ keystr[i])
P_T=""
for i in range(0,len(p_text)):
    char=chr(p_text[i])
    P_T += char
print(P_T)









