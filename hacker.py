import detectenglish 
from transposition import TransCipher
import math

def main():
    secretmessage1 = """"ccdnye ee.iCru.g ,
yy"noer ss   o-smda
 la an tpit aon rd
eube rwd e  itl, e, T i ney    bopm r aHiirgoa sfnunniewgA admcalteilas arclhrnbrtsneciefaee,t duarutr  ubirn litiapebatt o nciilt.hbnE"""

    secretmessage2 = """Cr sosoemd tiohus oohs au e oosr reHnvaawggcmtng eaaaagecgrehobrlrl sgrvrnkei, deayaia ecea e.t dern pkdt h tyr ete  sthevhy fuo 
 hcytphylaeoaulubYyerohoe!yn unnaryoonyuas 
 cR d ts uu p tibTseSt hiedrrwth teoedAoeaole  aiasigdc   xcnfclolnvuoiauecdpks oawkgebnnyrnioei!adsn   s n,ecp rn  it siwtci drhyigYfn sotriiny yeom!oogtem itpgouprueur aceutuh ust.rn mtsrostteorii
 thihkenieirf noIoaadi tennos dgn wtvasi  g.n ca  enieb smt 
 artasn o lm ehtRarya ucrnpeetsrhenep mcoe!"""

    specialmessage = "T,ebh aeaiklnnelksra ts yr,aou nucdd to tonMoros sr.W,sST ,kPg i uaetenrusd!tt !o Irssspa"

    #print(hack(secretmessage1))
    #print(hack(secretmessage2))

    print(hack(specialmessage))


def hack(text):
    print("Hacking...")

    for key in range(2, math.ceil((0.5 * len(text)))): #looping through every possible key (key must be between 2 and half the length of the text)
        message = TransCipher(text, key, False)
        print(key)
        message.decrypt()

        if detectenglish.isitenglish(message.plaintext) == True:

            print(message.plaintext[:50]) #printing the first 50 characters of the possible decrypted message
            
            confirmation = input("Please confirm correct decryption (input yes or no)") #ask the user if this decrypted message is correct

            if confirmation == 'yes':
                return (message.plaintext + ' key: ' + str(key))

            else:
                print("running more key possibilities")
                break
         
    # Loop through every possible key
        # Print key number
        # Decrypt message
        # Test if the decrypted message is in English
        # If it is (according to isitenglish()), 
            # print a portion of the message to the user and ask them to confirm
            # If the user confirms, return the decrypted message
            # If they deny, continue with the next key

    pass

if __name__ == '__main__':
    main()