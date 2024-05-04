import string # Get access to ascii

alphabet = string.ascii_lowercase

# Step 2a)
def encryption(word:string):
    shift = int(input("Type the Shift number: "))
    encryptedWord = ''
    
    for i in range(len(word)):
        pos = alphabet.index(word[i])
        if (pos + shift >= len(alphabet)):
            encryptedWord += alphabet[(pos + shift) - len(alphabet)]
        else:
            encryptedWord += alphabet[pos + shift]
    
    return encryptedWord

    
# Step 2b)
def decryption(word:string):
    shift = int(input("Type the Shift number: "))   
    decryptWord = ''
    
    for i in range(len(word)):
        pos = alphabet.find(word[i])
        if (pos - shift < 0):
            decryptWord += alphabet[(pos-shift) + len(alphabet)]
        else:
            decryptWord += alphabet[pos-shift]
            
    return decryptWord


# Step 1
def encryptOrDecrypt():
    answer = int(input("Type '1' to encrypt(encode) and '2' to decrypt(decode): "))
    if (answer not in (1,2)):
        return 'Exit'
    
    while (answer == 1 or answer == 2):
        if answer == 1:
            encrypt = input("Type word you want to encrypt: ").lower()
            return encryption(encrypt) 
        
        elif answer == 2:
            decrypt = input("Enter word you want to decrypt").lower()
            return decryption(decrypt)


  
def caesarCipher():
    while True:  # This will start an infinite loop
        answer = int(input("Type '1' to encrypt(encode), '2' to decrypt(decode), or '3' to exit: "))
        
        if answer == 3:  # If the user types '3', break the loop and end the function
            break

        elif answer == 1:
            encrypt = input("Type word you want to encrypt: ").lower()
            encryptedWord =  encryption(encrypt) 
            print(f"Encrypted word is: {encryptedWord}")
    
        elif answer == 2:
            decrypt = input("Enter word you want to decrypt: ").lower()
            decryptWord = decryption(decrypt)
            print(f"Decrypted word is: {decryptWord}")

        
print(caesarCipher())
    


# shift = 1
# newWord = ''
# for i in range(len(alphabet)):
#     if (i + shift >= len(alphabet)):
#         # shift needs to start from 0
#         newWord += alphabet[i+shift - len(alphabet)]
#     else:
#         newWord += alphabet[i+shift]
# print(alphabet)
# print(newWord)

# decryptWord = ''
# for i in range(len(newWord)):
#     if (i - shift < 0):
#         decryptWord += newWord[i - shift + len(newWord)]
#     else:
#         decryptWord += newWord[i-shift]
        
# print(decryptWord)