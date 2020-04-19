'''
CaesarCipher encrypts and decrypts a given message
   @author: Shelby Neal
   Emplid: 6030859
   Email: ssn287@email.vccs.edu
   Purpose: Programming Assignment #5
'''

key = 'abcdefghijklmnopqrstuvwxyz' #creates the list of characters that can be encrypted
choice = input("\n\tEnter from the following - q (quit), d (decode), e (encode): ")
while choice != 'q':
    if choice == 'e': #encoding
        msg = input("\n\tEnter a message to encode:") #user inputs message to be encrypted
        pos = int(input("\n\tEnter a number of rotation: ")) #user inputs number of times alphabet is to be shifted
        newKey = key[pos:] + key[:pos] #new shifted alphabet is generated
        result = '' #result initialized
        for i in msg: #transverse the plain text
            if i in key: #if the character is in the list of encrypted characters
                val = key.index(i) #shift the list by pos
                result += newKey[val] #add the encrypted letter to result
            else: #otherwise, the character is not encrypted
                result += i
        print("\n\tThe encoded message is: ", result) #prints the encrypted message
    elif choice == 'd': #decoding
        decResult = '' #result initialized
        for i in result: #transverse the cipher text
            if i in key: #if the character is in the list of encrypted characters
                decPos1 = key.find(i) #find the position of the character
                decPos2 = (decPos1 - pos) % 26 #find the original position of the character in the list
                decVal = key[decPos2] #character is assigned
                decResult += decVal #add the decrypted letter to result
            else: #otherwise, the character is not decrypted
                decResult += i
        print("\n\tThe decoded message is: ", decResult) #prints the decryupted message
    else: #ValueError check
        print("\n\tInvalid Selection")
    choice = input("\n\tEnter from the following - q (quit), d (decode), e (encode): ") #loop is repeated until user select 'quit'