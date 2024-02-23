import art

print(art.divider)
print(art.logo)
print(art.divider)
should_end = False
while not should_end:
    while True:
        try: 
            direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
            if direction == 'e' or direction == 'd':
                break
            else: print("Invalid Entry! Please enter 'd' or 'e'")
        finally:
            if direction == 'e':
                print("OK, lets encode your message")
            elif direction == 'd':    
                print("Alright, let's decode your message")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
                    

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def encrypt(text, shift, direction):
        ciphered = ''
        if direction == 'e':
            for letter in text:
                if letter in alphabet:
                    i = alphabet.index(letter)
                    if i >= (26 - shift):
                        new_i = i - (26-shift)
                    else: new_i = i + shift
                    ciphered += alphabet[new_i]
                else: ciphered += letter            
        elif direction == 'd':
            for letter in text:
                if letter in alphabet:    
                    i = alphabet.index(letter)
                    if i <= (shift - 1):
                        new_i = i + (26-shift)
                    else: new_i = i - shift
                    ciphered += alphabet[new_i]
                else: ciphered += letter    
        print("\n\n            RESULT:\n\n")
        print(ciphered)

    encrypt(text=text, shift=shift, direction=direction)
    restart = input("\n\n\n               Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")

# encrypt(text = input("Type your message:\n").lower(),shift = int(input("Type the shift number:\n")), direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n"))