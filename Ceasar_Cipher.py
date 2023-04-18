from alphabet import alphabet


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


print(text[0])
def encrypt(text, shift):
    cipher_text=""
    for x in text:
        cipher_text+=alphabet[alphabet.index(x)+shift]
    print(cipher_text)

encrypt(text, shift)
