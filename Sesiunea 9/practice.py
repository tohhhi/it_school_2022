#1. Definiti o matrice 5 x 5 si afisati numerele de pe diagonala principala si numerele de pe diagonala secundara.


#1 2 3
#4 5 6
#7 8 9

 
#Diagonala principala 1 5 9 
#Diagonala secundara 3 5 7


 # cum putem returna mai multe valori dintr o functie


matrice = [
    
    [33, 44, 55, 66, 77],
    [22, 11, 99, 88, 21],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]



print("Diagonala principala:",matrice[0][0],matrice[1][1],matrice[2][2],matrice[3][3],matrice[4][4])
print("Diagonala secundara:",matrice[0][-1],matrice[1][-2],matrice[2][-3],matrice[3][-4],matrice[4][-5])