banned_countries = ('Romania', 'Lituania', 'Norvegia')


list_banned = list(banned_countries)

same_element = True

if len(banned_countries) == len(list_banned):
    for i in range(len(banned_countries)):
        if banned_countries[i] != list_banned[i]:
            same_element = False
            break


print("Lista nemodificata:",same_element)