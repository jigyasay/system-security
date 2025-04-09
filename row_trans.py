import math
def encrypt(text,key):
    cipher_text = []
    key_lst=list(key)
    key_lst=sorted(key_lst)
    msg_lst=list(text)
    col=len(key)
    row=math.ceil(len(text)/col)
    ttl_null=row*col-len(text)
    msg_lst.extend('_'*ttl_null)
    matrix=[msg_lst[i:i+col] for i in range(0,len(msg_lst),col)]
    k_idx=0
    for _ in range(col):
        cur_idx= key.index(key_lst[k_idx])
        for row in matrix:
            cipher_text.append(row[cur_idx])
        k_idx+=1
    return ''.join(cipher_text)
            
def decrypt(text,key):
    key_lst=list(key)
    key_lst=sorted(key_lst)
    msg_lst=list(text)
    col=len(key)
    row=int(len(text)/col)
    matrix=[['']*col for _ in range(row)]
    k_idx=0
    idx=0
    for _ in range(col):
        cur_idx = key.index(key_lst[k_idx])
        for r in range(row):
            matrix[r][cur_idx]=msg_lst[idx]
            idx+=1
        k_idx+=1
    return ''.join(sum(matrix,[]))


def main():
    text=input("Enter the text: ")
    key=input("Enter the key: ")
    encrypted_text=encrypt(text,key)
    encrypted_text=encrypt(encrypted_text,key)
    print("Encrypted Text: ",encrypted_text)
    decrypted_text=decrypt(encrypted_text,key)
    decrypted_text=decrypt(decrypted_text,key)
    ttl_null=decrypted_text.count('_')
    if(ttl_null>0):
        decrypted_text=decrypted_text[:-ttl_null]
    print("Decrypted Text: ",decrypted_text)
    

if __name__=="__main__":
    main()