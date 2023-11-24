import os
import sys
import time

import transpositionEncrypt


def main():
    inputFilename = 'ces.txt'
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt'  # 'encrypt' or 'decrypt'

    if not os.path.exists(inputFilename):  # if input file does not exist, quit
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    if os.path.exists(outputFilename):  # give user a chance to quit
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %
              (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # read the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # time the encryption/decryption
    startTime = time.time()
    if __name__=='__main__':
     if myMode == 'encrypt':
        transpositionEncrypt.encryptMessage(myKey, content)