alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift, direction):
    ciphered = ''
    if direction == 'e':
        for letter in text:
            i = alphabet.index(letter)
            if i >= (26 - shift):
                new_i = i - (26-shift)
            else: new_i = i + shift
            ciphered += alphabet[new_i]
        print(ciphered)        
    elif direction == 'd':
        for letter in text:
            i = alphabet.index(letter)
            if i <= (shift - 1):
                new_i = i + (26-shift)
            else: new_i = i - shift
            ciphered += alphabet[new_i]
        print(ciphered)     
# encrypt('civiliztion', 5, 'e')
# encrypt('hnanqnefynts',5, 'd')

encrypt(text = input("Type your message:\n").lower(),shift = int(input("Type the shift number:\n")), direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n"))