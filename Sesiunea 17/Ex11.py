

#11) Print a justified string histogram for lorem variable.
#    EX:
#    l ................ 10
#    i ................ 20
#    j .................33


lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

clean_words = []

words = lorem.split()


for word in words:
    clean_words.append(word.lower().strip(".,'"))
    

max_len = 0

for word in clean_words:
    if (len(word)) > max_len:
        max_len = len(word)


passed_words = []

for word in clean_words:
    if word not in passed_words:
        print(word.ljust(max_len + 10, "."), clean_words.count(word))
        passed_words.append(word)
    



    


