# Code Decode

## Challenge

Around 5 years ago, I made this killer program that encodes the string into a cyphertext. The unique feature of this program is that for the same exact plaintext, it generates a different cyphertext every time you run the program. Yesterday I was nosing around in some old stuff and found an encrypted message!

```
2njlgkma2bv1i0v}22lv19vuo19va2bvl2{-5x
```

Sadly I realized that I lost the decryption program. I have the encryption program though. Do you think you can help me out and decrypt this message for me?

### Given encrypter program:

```python
from random import choice

inputstring = input("Enter plaintext: ")


def read_encryption_details():
    with open("cypher.txt") as file:
        encrypt_text = eval(file.read())
        encrypt_key = choice(list(encrypt_text.keys()))
        character_key = encrypt_text[encrypt_key]
    return encrypt_key, character_key


def create_encryption(character_key):
    charstring = "abcdefghijklmnopqrstuvwxyz1234567890 _+{}-,.:"
    final_encryption = {}
    for i, j in zip(charstring, character_key):
        final_encryption[i] = j
    return final_encryption


def convert_plaintext_to_cypher(inputstring, final_encryption, encrypt_key):
    cypher_text = ""
    for i in inputstring:
        cypher_text += final_encryption[i]
    cypher_text = encrypt_key[:3] + cypher_text + encrypt_key[3:]
    return cypher_text


encrypt_key, character_key = read_encryption_details()
final_encryption = create_encryption(character_key)
cypher_text = convert_plaintext_to_cypher(
    inputstring, final_encryption, encrypt_key)

print(cypher_text)
```

## Solution

1. Study the code and understand the encryption process
   - A file called [cypher.txt](cypher.txt) is read, and evaluated into a dictionary
   - From the dictionary's keys, one is chosen as random
   - Once the key is chosen, the corresponding values are also aquired
   - Next, the aquired values are assigned to each letter in the alphabet<br>
     Ex: `a->k, b->y, c->e etc`<br>
     to generate its own "language" that plaintext can be translated to
   - Plaintext is then converted to this new "language" that was generated above
   - IMPORTANT: The last step is when, after encoding, the key that can decode this is split into two parts
   - One part is prepended to the encoded string, the other is appended to the resultant string
     Final cypher text = <key part 1><encoded text><key part 2>
2. Write a decrypter
   - Take cyphertext as input
   - Take first three characters from the string and last three characters from the string
   - These 6 characters make the key, and the rest of the code make the ciphertext.<br>
     <img src="solution_imgs\code_decode_1.png" alt="drawing" width="400"/>
   - Read "cypher.txt" and find the value for the key that was made in the last step
   - Using the values, assign each character in the value to the respective alphabet<br>
     Ex: `k->a, y->b, e->c`
   - Using this decoder, pass the cyphertext and generate plaintext to get the key

### Decrypter for encryption

```python
cypher_text = input("Enter cypher text: ")

key = cypher_text[:3] + cypher_text[-3:]
cypher_text = cypher_text[3:-3]

with open("cypher.txt") as file:
    decrypt_key = eval(file.read())[key]

charstring = "abcdefghijklmnopqrstuvwxyz1234567890 _+{}-,.:"
final_decryption = {}
for i, j in zip(charstring, decrypt_key):
    final_decryption[j] = i

plaintext = ""
for i in cypher_text:
    plaintext += final_decryption[i]

print("Plaintext =",plaintext)
```

<img src="solution_imgs\code_decode_2.png" alt="drawing" width="500"/>

### flag: dsc{y0u_4r3_g00d_4t_wh4t_y0u_d0}
