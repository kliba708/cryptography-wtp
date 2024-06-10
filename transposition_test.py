import random,sys
import string
import math
from transposition import TransCipher

def main():
    random.seed(42) # this way if something fails, we can replicate the same problem to see what went wrong
    numtests = 50   # set a number of tests

    # run tests
    for i in range(numtests):
        message = (''.join(random.choices(string.ascii_uppercase, k=20)))

        message_length = len(message)

        print(i)
        print(message)

        # looping through all possible key values (from two to half the length of the message)
        for key in range(2, math.ceil((0.5 * message_length))): 

            cipher_instance = TransCipher(message, key)
            cipher_instance.encrypt()

            print(cipher_instance.encrypted)

            cipher_instance.decrypt()

            print(cipher_instance.plaintext)

        pass
    sys.exit()


        # generate random text  
        # shuffle text  
        # print the test number and a snippet of the text  

        # loop through all possible keys 
            # create an instance of TransCipher 
            # encrypt and decrypt message  
            # check we end up with the original text
                # if we don't, print an error message and show the original text, ciphertext, and decrypted plaintext
                # end the tests using sys.exit()
        
        # if we make it through the loop, print that this test was passed

if __name__ == '__main__':
    main()