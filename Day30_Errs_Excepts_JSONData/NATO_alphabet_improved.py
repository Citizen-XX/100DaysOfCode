import pandas as pd

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
file_path = r'Day30_Errs_Excepts_JSONData\nato_phonetic_alphabet.csv'
df = pd.read_csv(file_path)
phonetic_dict = {values.letter:values.code for (index,values) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
only_letters = False
while not only_letters:
    user_input = input('Input a word: ').upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in user_input]
        only_letters = True
    except KeyError as e:
        print('Sorry, only letters in the alphabet please')
    else:
        print(phonetic_list)
