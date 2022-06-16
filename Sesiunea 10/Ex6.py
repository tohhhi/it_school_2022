# 6) scrieti o functie (get_week_days) care returneaza un dictionar ce contine zilele saptamanii, mapate de forma "luni": 1
# functia trebuie sa primeasca un param. optional de tip bool (work_week) cu val default False;
# Daca work_week este adevarat atunci se va returna un dict. ce contine doar zilele lucratoare.

work_week = False

dict1 = {
    "luni": 1,
    "marti": 2,
    "miercuri": 3,
    "joi": 4,
    "vineri": 5,
    "sambata": 6,
    "duminica": 7
}


def get_week_days(work_week):
    if work_week == True:
        for keys in list(dict1.keys()):
            if dict[keys] > 6:
                del dict1[keys]
                print(dict1)

    




get_week_days(True)







