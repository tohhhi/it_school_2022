# 3) Make a script which encrypts a string using Caesar cipher with key 20, use a function to generate a dict representing the new alphabet
#    A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
#    Y	Z   A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X
#    caesar {
#        "A": "Y",
#        "B": "Z",
#        "C": "A"
#    }

#    def get_alphabet(key):
#        generate new alphabet
#        return dict with alphabet

#    def crypt(msj, key):
#        alphabet = get_alphabet(key)
#        return msaj cripta

#    crypt("Mesajul", 20)


def cipher(key):
    for i in range(65,91):
        key = chr(i)
        print(key , end = " ")


print(cipher(B))