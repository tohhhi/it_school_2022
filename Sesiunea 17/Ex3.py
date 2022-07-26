# 3) Extract words from lorem variable and store them in a list.

lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

lista = []

lista.append(lorem.split()[10])
lista.append(lorem.split()[20])
lista.append(lorem.split()[30])
lista.append(lorem.split()[40])
lista.append(lorem.split()[50])
lista.append(lorem.split()[60])

print(lista)