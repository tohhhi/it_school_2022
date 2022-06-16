#7. Foloseste functiile de la pct. 4-6 pentru a calcula cate cuburi cu muchia de 18 metri
#sunt necesare pentru a umple un cilindru cu raza bazei de 20 m si inaltimea de 55 m.
#- Printeaza volumul cubului in metri cubi #### Volumul cubului: 20 m^3
#- Printeaza volumul cilindrului in metri cubi.
#- Printeaza rezultatul de la pct. 7
#- Toate valorile printate vor fi insotite de mesaje descriptive.


def volume_to_liters(value):
    return value ** 3 * 1000






def liters_to_mcub(liter):
    return liter / 1000


print("Volumul cubului:" , liters_to_mcub(volume_to_liters(18)) ,"m3")



