from pprint import pprint
from practice import py_text

text = "mihAI dinu"

calatori = [
    "Otavă Bogdan",
    "Greta Mihaela Geabelea",
    "Iustin Gabriel Manciu",
    "Corina Lungu",
    "Melissa Madalina Haj Abdo",
    "Gabriel Guțui",
    "George Valeanu",
    "Andreea-Simona Telegeanu",
    "Ionuț Alin Preda",
    "Arthur Timbalariu",
    "Cristian Laurentiu Șandor",
    "Alex Raul Bonat-Mihalca",
    "Artsanyo Dennis Kachi",
    "Sergiu Mihai Predel",
    "Marian-Gabriel Tohaneanu-Iatan",
    "Irina Florentina Barbu",
    "Cordos Simona",
]

# idx_virgula = py_text.find(",") # gaseste indexul sub-stringului cautat
# print(py_text[:idx_virgula])
"""
idx_virgula = -1
done = False
while not done:
    idx_virgula = py_text.find(",", idx_virgula + 1)
    if idx_virgula != -1:
        print(idx_virgula)
    else:
        done = True
"""

py_text.replace(" ", "") # inlocuire

# count
py_text.count(".")

# split, rupe in bucati dupa delimitator

# print(py_text)
propozitii = py_text.split(". ")

words = py_text.split()
clean_words = []

for word in words:
    clean_words.append(word.lower().strip(",.'[]{}():;-+=<>"))

# lungimea celui mai lung cuvant din lista
max_len = 0

for word in clean_words:
    if len(word) > max_len:
        max_len = len(word)

passed_words = []
for word in clean_words:
    if word not in passed_words:
        print(word.ljust(max_len + 10, "."), clean_words.count(word))
        passed_words.append(word)



# name = "Alin"
# surname = "Preda"

# print(name.ljust(10, "_"))
# print(surname.ljust(10, "_"))