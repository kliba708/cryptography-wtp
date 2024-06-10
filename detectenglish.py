# create dictionary of words in dictionary.txt
def create_dict(filename):
    dictionary_file = open(filename) # opens file so we can read from it
    english_words = {} # creates empty dictionary
    for word in dictionary_file.read().split('\n'): # loops through file, splitting at line breaks
        english_words[word] = None # adds current word to the dictionary as a key, with a value of None
    dictionary_file.close() # closes file after we are done reading it
    return english_words 

english_words = create_dict('dictionary.txt')
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ' \t\n'

# remove extra symbols and punctuation from message
def remove_symbols(message):

    letters = []
    for symbol in message:
        if symbol in alphabet:
            letters.append(symbol) #adding all of the letters to the letters list --> basically removing the symbols by leaving them out of this list. 

    return ''.join(letters) #this is returning the message from the list without any symbols!

    """ returns the message, but only with characters in alphabet"""
    pass 

def count_words(message):

    message = message.upper()
    message = remove_symbols(message)

    words = message.split()

    eng_counter = 0

    for word in words:
        if word in english_words:
            eng_counter += 1 
    return (eng_counter / len(words))


    """ returns ratio of english words over total possible words"""
    # turn everything uppercase and remove symbols
    # split message into 'words'
    # count how many of the 'words' are actually english words
        #i'll need to use the dictionary and then compare the word to the dictionary values to see if they match up
    # return ratio of english words over total 'words'
    pass 


def isitenglish(message, wordpercent=40, letterpercent=85):
    """ returns True if message is in English, False if not"""
    eng_check = count_words(message) * 100 >= wordpercent
    #should return true if the message word count times 100 (to make it a percent) is greater than or equal to 40% (the value of word percent)

    letter_count = len(remove_symbols(message))

    message_letterpercent = (letter_count / len(message)) * 100

    letter_match = message_letterpercent >= letterpercent
    # this should return true if the percent of letters in the message is greater than or equal to the set amount

    return eng_check and letter_match

    # word percent is how many words are in the dictionary
    # letter percent is how many characters are in bigalphabet
    pass

def main():
    eng_test = isitenglish("Is this english asdfas asdfas ") 
    print(eng_test)

    pass

if __name__ == "__main__":
    main()
