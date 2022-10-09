"""
Project Name: PRNG & Stream Cipher
Project Description: Write a program that uses a random seed and a pseudo random number generator to
encrypt/decrypt a long string. This program will use the system time as the seed. 
Programmer: Michaela Pierce
Date: 10/09/22
UNCW, CSC 592 - Introduction to Cryptography
Relative Code by: phasing17, 
                  url: https://www.geeksforgeeks.org/pseudo-random-number-generator-prng/
"""

#modules imported 
import random # generates random numbers
import time # imports system time

# encrypt function
def encrypt(string, key):
    #converts string to bytes 
    enc_string = string.encode()
    byte_array = bytearray(enc_string)
    string_len = len(string)

    counter = 0 
    enc_array = []
    for i in range(counter, string_len): # for each character in string 
        enc_array. append ((byte_array[i] ^ key [i])) # XOR operator (^)

    enc_byte = bytes(enc_array) #encrypt array of bytes 
    return enc_byte
    

# decrypt function
def decrypt (enc_string, key):
    #converts string to bytes 
    enc_array = bytearray(enc_string)
    string_len = len(enc_array)

    counter = 0
    dec_array = []
    for i in range(counter, string_len): # for each character in encrypted string 
        dec_array.append((enc_array [i] ^ key [i])) # XOR operator (^)

    dec_byte = bytes(dec_array).decode() # decrypt array of encrypted bytes 
    return dec_byte

# Driver Code 
if __name__ == "__main__":
    # 1. Use the system time for the random seed (see this link). Prefer to use int(time.time())
    #    for random seed.
    seed = int(time.time())
    random.seed(seed)
    string = "Hello World!"

    # 2. Use the random.randbytes (only available in python 3) to generate a sequence of
    #    random bytes (as a one-time pad used as a key).
    key = random.randbytes(len(string))

    # 3. Use ‘bytearray’ to convert a string to array of bytes
    # 4. Use XOR operator (^) in python over the input string and key to encrypt the string.
    enc_byte = encrypt (string, key)
    dec_byte = decrypt (enc_byte, key)
    
    #prints all output 
    print ("Random seed = ", seed)
    print ("String = ", string)
    print ("Key = ", key)
    print ("CipherText = ", enc_byte)
    print ("PlainText = ", dec_byte)
