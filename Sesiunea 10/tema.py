"""

1) Write a function to set None at a specified key in a dict
2) Remove all the items from months dict with value greater then 6
3) Make a script which encrypts a string using Caesar cipher with key 20, use a function to generate a dict representing the new alphabet
    A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
    Y	Z   A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X
    caesar {
        "A": "Y",
        "B": "Z",
        "C": "A"
    }

    def get_alphabet(key):
        generate new alphabet
        return dict with alphabet

    def crypt(msj, key):
        alphabet = get_alphabet(key)
        return msaj cripta

    crypt("Mesajul", 20)

4) Make list of dictionaries, each dictionaries contains the following attributes: name, age, gender; Read those info from keyboard input.
5) sort list by users age

6) scrieti o functie (get_week_days) care returneaza un dictionar ce contine zilele saptamanii, mapate de forma "luni": 1
functia trebuie sa primeasca un param. optional de tip bool (work_week) cu val default False;
Daca work_week este adevarat atunci se va returna un dict. ce contine doar zilele lucratoare.

P1 - Phone Agenda
Utilizatorul interactioneaza cu consola, la inceput este afisat un meniu
numerotat, utilizatorul introduce un nr, urmat de Enter.

Fiecare intrare din meniu porneste un flux operational separat care atunci cand se incheie
se doreste a se revini la meniul principal.

Numele din agenda trebuie sa fie unice.

Meniu:
1. adauga contact
2. cauta contact
3. sterge contact

Fuxuri:
1. Adaugare contact
    citeste nume
    citeste nr tel
    intreaba daca doreste sa adauge alt nr.
    daca da repeta pasii
    daca nu revino la meniu principal

2. cauta contact
    introdu cateva litere > Enter
    daca stringul introdus face parte din numele din agenda
    daca sunt gasite contacte acestea sunt afisare in ordine alfabetica
    de forma:

    1. Mihai
    2. Vasile

    0: Revino la meniu

    Utilizatorul introduce un nr. corespondent numelui pe care vrea sa il vada.
    Contactul va fi afisat de forma:

    +----------------------------+
    Nume:  Xxxxxx
    Telefon: xxxx-xxx-xxx
    +----------------------------+

    0: revino la lista


3. sterge contact
    introdu numele complet
    daca acesta exista va fi sters
    daca nu o eroare este afisata.
    apoi se revine la meniu principal

"""