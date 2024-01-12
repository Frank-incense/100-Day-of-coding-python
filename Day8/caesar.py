alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, key, direct):

    cipher = ""
    for i in range(len(message)):
        if message[i] in alphabet:
            if direct == "encode":
                position = (alphabet.index(message[i]) + key) % 26
                cipher += alphabet[position]
            elif direct == "decode":
                position = (alphabet.index(message[i]) - key) % 26
                cipher += alphabet[position]
        else:
            cipher += message[i]

    print(f"The encoded text is {cipher}")


from art import logo

print(logo)

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, key=shift, direct=direction)
    
    response = input("Want another round? yes or no: \n").lower()
    if response == "no":
        end = True