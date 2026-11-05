# Day 8 of 100

# Practice functions:
# import greet
# greet.greet("Ryosuke")
# greet.greet_with("Ryosuke", "Japan")

# Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = True

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_letter = alphabet[new_position]
        cipher_text += cipher_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount + 26
        cipher_letter = alphabet[new_position]
        cipher_text += cipher_letter
    print(f"The encoded text is {cipher_text}")

while repeat == True:
    crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt: " )
    message = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    shift = shift % 26

    if crypt == 'encode':
        encrypt(plain_text=message, shift_amount=shift)
        rep = input("Do you wanna encode or decode other message? Y or N: ")
        if rep == 'Y' or rep == 'y':
            repeat = True
        else:
            repeat = False
    else:
        decrypt(plain_text=message, shift_amount=shift)
        rep = input("Do you wanna encode or decode other message? Y or N: ")
        if rep == 'Y' or rep == 'y':
            repeat = True
        else:
            repeat = False