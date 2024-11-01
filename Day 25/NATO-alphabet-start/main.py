import pandas


data = pandas.read_csv("Day 25\\NATO-alphabet-start\\nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
phonetic_dict = {row.letter:row.code for (index,row) in df.iterrows()}

word = str(input("Enter a word: ")).upper()
res = [phonetic_dict[char] for char in word]
print(res)




