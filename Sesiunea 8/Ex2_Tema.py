#2. Scrieti o functie care returneaza True daca lista primita ca param. este sortata,
#altfel returneaza False.





numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [6, 1, 10, 2, 5, 7, 9]



def sortare_lista(sort_list):
     
    if sort_list.sort():
        return len(sort_list.sort) == 1
   

sortare_lista(numbers)
    



#numbers.sort()
#print(numbers)

#b.sort()
#print(b)
    
