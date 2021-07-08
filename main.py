import pandas


data = pandas.read_csv("./nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = (input("Enter a word: ")).upper()
word = [letter for letter in list(user_input)]
result = [alphabet_dict[letter] for letter in word if alphabet_dict[letter]]

print(result)
