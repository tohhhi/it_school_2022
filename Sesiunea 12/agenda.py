"""
1. Scrie o clasa care repr. o Agenda (Notebook).
Atribute:
    - nr pagini
    - culoare
    - continut - lista de stringuri ["continut pagina", "continut pag."]

Metode:
    - scrie in Agenda
    - vezi nr de pag goale
    - vezi nr pag scrise

"""

class Notebook:

    def __init__(self):
        self.__nr_pagini = 120
        self.__culoare = "verde"
        self.__continut = list()

    def adaugare_continut(self, scrie):
        if self.__nr_pagini - len(self.__continut) == 0:
            pass
        else:
            self.__continut.append(scrie)
       
    def descriere_caiet(self):
        print("Caietul are", self.__nr_pagini,"de pagini.")
        print("Caietul este de culoare",self.__culoare,".")


    
        
    def nr_pagini_goale(self):
        return self.__nr_pagini - len(self.__continut) 
    
    def nr_pagini_scrise(self):
        return len(self.__continut)

caiet1 = Notebook()

caiet1.descriere_caiet()

caiet1.adaugare_continut("pag1")

caiet1.adaugare_continut("pag2")

caiet1.adaugare_continut("pag3")

caiet1.adaugare_continut("pag4")

caiet1.adaugare_continut("pag5")

caiet1.adaugare_continut("pag6")

caiet1.adaugare_continut("pag7")

caiet1.adaugare_continut("pag8")

caiet1.adaugare_continut("pag9")

caiet1.adaugare_continut("pag10")

caiet1.adaugare_continut("pag11")

caiet1.adaugare_continut("pag12")

print("pagini scrise:",caiet1.nr_pagini_scrise())

print("pagini goale ramase:",caiet1.nr_pagini_goale())







    








