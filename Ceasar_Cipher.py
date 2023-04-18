from alphabet import alphabet


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    cipher_text=""
    for x in text:
        cipher_text+=alphabet[alphabet.index(x)+shift]
    print(cipher_text)

def decrypt(cipher, shift):
    fixed_text=""
    for x in cipher:
        fixed_text+=alphabet[alphabet.index(x)-shift]
    print(fixed_text)

if direction=="encode":
    encrypt(text,shift)
elif direction=="decode":
    decrypt(text,shift)
else:
    print("Wrong input")