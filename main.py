import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet_dict)


def generate_list():
    user_input = (input("Enter a word: ")).upper()
    try:
        result = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_list()
    else:
        print(result)


generate_list()
