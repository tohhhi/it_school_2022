#1. Scrieti o functie care returneaza reversul unei liste. Lista primita ca parametru nu 
#trebuie modificata.


cars = ["Mercedes", "Audi", "BMW", "RENAULT"]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def func1(modify_list):
     modify_list.reverse()
     print(modify_list)


func1(numbers)

func1(cars)




