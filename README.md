# Pseudo-Random Number Generator (PRNG) & Stream Cipher
This project implements a simple encryption and decryption program using a pseudo-random number generator (PRNG) and stream cipher. The program uses the system time as a seed for the PRNG to generate a key, which is then used to encrypt and decrypt a string via the XOR operation. The goal is to demonstrate how PRNG can be applied to secure data by generating a random key based on the system time.

## Features
- Uses the system time as the seed for the PRNG.
- Encrypts and decrypts a string using a key generated from the PRNG.
- Utilizes Python's `random` module and `time` module.
- Demonstrates the use of XOR operation for encryption and decryption.


## Requirements
- Python 3.x (This program uses `random.randbytes` which is available in Python 3.9+)

## Installation & Usage

1. Clone the repository or download the source code.
2. Run the program using Python:

   ```bash
   python3 prng_stream_cipher.py
   ```

3. The program will print the following information:
    - Random seed used for generating the key
    - Original string
    - Generated key (in bytes)
    - Encrypted string (ciphertext)
    - Decrypted string (plaintext)

## Example Output
Below are 2 examples with 2 different system times and the output.

### Example 1 
![PRNGEx1](https://github.com/user-attachments/assets/0dc43451-6011-41e8-8305-3b464dd3e650)


### Example 2
![PRNGEx2](https://github.com/user-attachments/assets/92254c90-72f5-4470-9c07-c9a7f4c69112)


## Acknowledgements

- This project was inspired by a similar implementation by phasing17 on GeeksforGeeks: [Pseudo-Random Number Generator (PRNG)](https://www.geeksforgeeks.org/pseudo-random-number-generator-prng/).



