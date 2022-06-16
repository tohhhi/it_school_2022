#6. Intr-o cutie se află 300 de bile, numerotate cu numere începând de la unu, 
#din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. 
#Să se afle câte bile verzi sunt.




even_count = 0

for i in range(1, 301, 3):
    if i % 2 == 0:
       print(i,end = ' ')
       even_count = even_count + 1
print("Total bile verzi:",even_count)
        
        

    
        
        

        
        
        
        

        
        
    
        

 


