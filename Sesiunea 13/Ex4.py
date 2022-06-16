from datetime import datetime
from air_travel import Airplane, AirTrip, Ticket

calatori = [
    "Otavă Bogdan",
    "Greta Mihaela Geabelea",
    "Iustin Gabriel Manciu",
    "Corina Lungu",
    "Melissa Madalina Haj Abdo",
    "Gabriel Guțui",
    "George Valeanu",
    "Andreea-Simona Telegeanu",
    "Ionuț Alin Preda",
    "Arthur Timbalariu",
    "Cristian Laurentiu Șandor",
    "Alex Raul Bonat-Mihalca",
    "Artsanyo Dennis Kachi",
    "Sergiu Mihai Predel",
    "Marian-Gabriel Tohaneanu-Iatan",
    "Irina Florentina Barbu",
    "Cordos Simona",
]


d_time = datetime(2022, 6, 2, 12, 30)
a_time = datetime(2022, 6, 2, 13, 10)


trip1 = AirTrip("BUC", "TIM", d_time, a_time, 100)
airbus = Airplane(20, 4)

ticket_list = []

for name in calatori:
    ticket_list.append(Ticket(name, airbus.get_next_free_seat(), trip1))


for i in ticket_list:
    i.print_ticket()