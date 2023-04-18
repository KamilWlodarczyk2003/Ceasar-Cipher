from alphabet import alphabet
from art import logo

print(logo)


def Ceasar():
    question ="yes"
    while question=="yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))%26
        ceasar_text=""
        if(direction=="encode"):
            for x in text:
                if x in alphabet:
                    ceasar_text+=alphabet[alphabet.index(x)+shift]
                else:
                    ceasar_text+=x
        if(direction=="decode"):
            for x in text:
                if x in alphabet:
                    ceasar_text+=alphabet[alphabet.index(x)-shift]
                else:
                    ceasar_text+=x
        print(ceasar_text)
        question=input('If you want to continue type "yes", if not type anything else\n')

Ceasar()