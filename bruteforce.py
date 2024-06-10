import random
import caesar

secretmessage = "LjwiHxDiorpDAnixDCivHiBnlAnCivnBBjpn)"
secretmessage2 = "!vprmwBoam!rKGmJrlyymyrnEAmnmpvCurEmGunGlFmABGmnFmrnFLmGBmunpx"

symbols = caesar.symbols

def bruteforce(plaintext):
    for key in range(len(symbols)): #setting the length of time that this for loop must run for --> we are going through every possible key value there is

        decrypted = '' #making an empty string for decrypted letters, just like for encrypted letters (/symbols) in caesar.py


        for letter in plaintext:

            index_num = symbols.find(letter) #this should find the index number of the letter (/symbol) in the message
            index_num -= key #subtracting the value of the key from the index number value (basically what I did in the decryption portion of the caesar file)

            decrypted += symbols[index_num] #same idea as the code in the caesar.py file

        print(decrypted + " " + str(key))
    


    """Inputs a plaintext string and prints out all possible decryptions"""
    pass

    # Loop through every possible key
    # Print the key and the decrypted message for the user
    # Use your functions from caesar.py, i.e. caesar.encrypt(message,key)

bruteforce(secretmessage) 
bruteforce(secretmessage2)

#success on printing out the secret messages and the keys next to them!!