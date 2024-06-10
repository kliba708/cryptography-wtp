import random

######## 1 ########
# To begin, we need to create the "wheel", aka the alphabet we will shift. We can use a string:
'''
alphabet = "abcdefghijklmnopqrstuvwxyz "

def encrypt(message, key):
    encrypted = ''
    message = message.lower() #since alphabet string is lowercase, I figured that I should make all letters of the message lowercase as well. 
    
    for letter in message.lower():
        pre_ciph = (alphabet.find(letter) + key) % len(alphabet) # finds the index number of each letter in the message and then adds the key value to that number. Then, divides that number by 26 and returns the remainder. 
        
        #also I had to split it up bc I didn't know how to put it all together!!
        encrypted += alphabet[pre_ciph]  
        #calling the value returned from the remainder above as the index number of alphabet #adding each encrypted letter to the variable encrypted

    return encrypted
'''

"""Inputs plaintext message (str) and key (integer). Returns encrypted message (str)"""
    

######## 2 ########
# Let's test the function and see what an encrypted message will look like
#print(encrypt('this is a test message', 3))
#print(encrypt('Drop the $$$ at 2408 Elms ST.',7))

######## 3 ########
symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*,()' " 

def encrypt_symbols(message, key):
    encrypted = '' 
    
    for letter in message:
        pre_ciph = (symbols.find(letter) + key) % (len(symbols))
        encrypted += symbols[pre_ciph]  

    return encrypted
 
def decrypt(message, key):
    key = - key
    decrypted = ''

    for letter in message:
        pre_ciph = (symbols.find(letter) + key) % (len(symbols))
        decrypted += symbols[pre_ciph]  

    return decrypted

######## 4 ########
test = "Hello world"
key = random.randrange(1, len(symbols))


encrypt_test = encrypt_symbols(test, key)

print(encrypt_symbols(test, key)) 

print(decrypt(encrypt_test, key)) 
