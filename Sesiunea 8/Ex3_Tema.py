#3. Scrieti o functie care primeste doua liste ca parametri. Listele contin numere intregi.
#Fct. returneaza o singura lista formata din inmultirea dupa cum urmeaza: primul elem. din prima 
#lista X primul elem. din a 2-a lista .... etc.
#[1, 2, 3]
#[3, 4, 6]
#=> [3, 8, 18]


list_number_1 = [1, 2, 3]

list_number_2 = [3, 4, 6]

list_number_3 = [5, 10 ,15]

list_number_4 = [15, 10, 5]



def multiply(list_1,list_2):
    print([a*b for a,b in zip(list_1,list_2)])



multiply(list_number_1,list_number_2)

multiply(list_number_3,list_number_4)