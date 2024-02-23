alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    hold = []
    new_hold = []
    for letter in str(text):
        hold.append(alphabet.index(letter))
    print(hold)    
    for i in hold:
        if i >= (26 - shift):

encrypt('civilization')