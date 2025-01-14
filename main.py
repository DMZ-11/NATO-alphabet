import pandas

df = pandas.read_csv("nato_alphabet.csv")

# Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name: ").upper()
nato_name = [nato_dict[letter] for letter in name]

print(nato_name)
