import math

class TransCipher:
    def __init__(self, message, key, isplaintext = True):
        '''
        Message: str, key: int, isplaintext: bool. isplaintext should be True if message is in plaintext, and False if message is in ciphertext.
        '''
        self.key = key
        if isplaintext: 
            self.plaintext, self.encrypted = message, None
        else: 
            self.plaintext, self.encrypted = None, message


    def encrypt(self):

        columns = [""] * self.key 

        rows = int(math.ceil((len(self.plaintext)) / int(self.key))) #need to divide message length by number of columns, then round up 

        #blank_box = ((rows * self.key) - len(self.plaintext)) #so this is supposed to represent those shaded boxes at the end... I just multipled the number of rows by columns to find the total number of boxes, then subtracted the length of the plaintext from that number. 

        message_index = 0 #this is the message index (aka each letter)

        # i indicates column number
    
        for i in range(0, len(columns)): # so we are going through each of the columns... 
            message_index = i

            for row in range(0, rows):
                columns[i] += self.plaintext[message_index]  #adding the letter to the column
                message_index += self.key

                if message_index >= len(self.plaintext):
                    break

        # so now I need to join together the columns into the final encrypted string. 

        self.encrypted = "".join(columns)

        return self.encrypted

        pass

    def decrypt(self):  

        column_num = int(math.ceil((len(self.encrypted)) / int(self.key))) #need to divide message length by number of rows, then round up 

        rows_num = self.key

        blank_boxes = (column_num * self.key) - len(self.encrypted) 

        self.plaintext = [''] * column_num   #making a list of empty strings 

        #starting the current column and row at 0
        column = 0
        row = 0

        for letter in self.encrypted:
            self.plaintext[column] += letter
            column += 1

            #if the current column is the last column, or the current column is the second to last column and the current row is greater than or equal to the number of rows minus the number of blank boxes

            ## (trying to account for the blank boxes and getting to the end of the columns and going back to the beginnning)

            if (column == column_num) or (column == column_num - 1 and row >= (rows_num - blank_boxes)): 
                column = 0  #reset the column back to the first one
                row += 1   # move to the next row

        self.plaintext = ''.join(self.plaintext)

        return self.plaintext
    
        pass

def main():
    # Uncomment the following when you are ready to test your code
    test = TransCipher("WTP is awesome!!", 3)
    test.encrypt()
    print(test.encrypted)
    test.decrypt()
    print(test.plaintext)
    
    #secret = TransCipher("Cusdes gol er wnayc togtorsorriuye kaorpebitn tmen", 7, False)
    #secret.decrypt()
    #print(secret.plaintext)


if __name__ == '__main__':
    main()

'''
test = TransCipher("This is a test!", 6, True)

encrypted_test = test.encrypt()

de_test = TransCipher(encrypted_test, 6, False)

print(encrypted_test) 
print(de_test)
# test of the encryption is a success!!!

'''
