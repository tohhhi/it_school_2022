


def DNA_strand(dna):
    dna_list = list(dna)
    for i in dna_list:
    
        if i == "A":
            i = "T"
        elif i == "T":
            i = "A"
        
        if i == "C":
            i = "G"
        elif i == "G":
            i = "C"
        
         
        print(i, end=(""))

    
    

   

    
DNA_strand("GTAT")





