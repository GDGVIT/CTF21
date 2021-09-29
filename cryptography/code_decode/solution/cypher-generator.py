from random import sample, shuffle

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
              'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
              '9', '0', ' ', '_', '+', '{', '}', '-', ',', '.', ':']
key_dict = {}
count = 0

while count != 300:
    key = "".join(sample(characters, 6))
    if key not in list(key_dict.keys()):
        count += 1
        shuffle(characters)
        key_dict[key] = "".join(characters)

with open("cypher.txt", 'w+') as file:
    file.write(str(key_dict))
