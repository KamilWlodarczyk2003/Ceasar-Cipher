from alphabet import alphabet


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def Ceasar(direction, text, shift):
    ceasar_text=""
    if(direction=="encode"):
        for x in text:
            ceasar_text+=alphabet[alphabet.index(x)+shift]
    if(direction=="decode"):
        for x in text:
            ceasar_text+=alphabet[alphabet.index(x)-shift]
    print(ceasar_text)

Ceasar(direction,text,shift)