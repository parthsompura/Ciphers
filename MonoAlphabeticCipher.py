key=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','','x','c','v','b','n','m']
plaintext=input("Enter Plaintext: ")
c=[]
p=[]
for i in range(0,len(plaintext)):
    c.append(key[ord(plaintext[i])-97])
print("Ciphertext: ")
print(c)
for i in range(0,len(c)):
    for j in range(0,len(key)):
        if(c[i]==key[j]):
            p.append(chr(j+97))
print("Plaintext: ")
print(p)
