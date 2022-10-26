#I've encrypted the flag with my secret key, you'll never be able to guess it.
#Remember the flag format and how it might help you in this challenge!
#0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
input_str=bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(input_str)
k="crypto{"
key=""
plaintext=""
for i in range (len(k)):
    key=key+chr(ord(k[i]) ^ input_str[i])
i=0
key=key+'y'
while (i<len(input_str)):
    l=0
    while (l<len(key)):
        if (i == len(input_str) and l<len(key) ):
            break
        plaintext = plaintext + chr( ord(key[l]) ^ input_str[i]) 
        l+=1
        i+=1
print(plaintext)

