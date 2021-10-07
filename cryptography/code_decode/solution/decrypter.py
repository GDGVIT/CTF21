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

print("Plaintext =", plaintext)
