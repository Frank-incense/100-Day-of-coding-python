import pandas

alphabet = pandas.read_csv('./Day26/NATO-alphabet/nato_phonetic_alphabet.csv')

userInput = input('Input a word: ').upper()

letters = [letter for letter in userInput]
nato_dict = {row.letter:row.code for index, row in alphabet.iterrows()}

nato = [nato_dict[letter] for letter in letters]
print(nato)