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


print(text.capitalize()) # Mihai dinu 
print(text.title()) # Mihai Dinu

print(text.endswith("x")) # verifica daca un string se termina intr-un sub-string
print(text.startswith("A"))

print(text.lower()) # mihai dinu
print(text.upper()) # MIHAI DINU

# for i in calatori:
#     if i.startswith("A"):
#         print(i)

# daca un sub-string face parte dintr-un string
# print("x" in text)

# for i in calatori:
#     if "ale" in i:
#         print(i)