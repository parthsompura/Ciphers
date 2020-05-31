plaintext=input("Enter Plaintext: ")
key=int(input("Enter Key: "))
c=[]
p=[]
for i in range(0,len(plaintext)):
    c.append(chr(ord(plaintext[i])+key))
print(c)
for i in range(0,len(c)):
    p.append(chr(ord(c[i])-key))
print("Plaintext")
print(p)
