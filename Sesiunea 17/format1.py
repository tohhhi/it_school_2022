from datetime import datetime


toy = "car"
# %s -> aici vine un string
new_string = "This is a %s" % toy

first_name = "Mihai"
last_name = "Dinu"
age = 20

print("Prenume: %s | Nume: %s | Varsta: %d" % (last_name, first_name, age))


def get_titles(lang):

    if lang == "ro":
        return {
            "title": "factura",
            "client_name": "nume client",
            "client_address": "adresa",
            "iban": "IBAN",
        }

    if lang == "en":
        return {
            "title": "invoice",
            "client_name": "client name",
            "client_address": "address",
            "iban": "account number",
        }


class Client:
    def __init__(self, name, address, iban) -> None:
        self.name = name
        self.address = address
        self.iban = iban


class Invoice:
    def __init__(self, client) -> None:
        self.client = client

    def print_invoice(self, lang):
        inv_len = 70
        strings = get_titles(lang)

        print(f"{strings['title'].title():*^{inv_len}}")
        print(
            f"{strings['client_name'].title()}:"
            f"{self.client.name:>{inv_len - 1 - len(strings['client_name'])}}"
        )
        print(
            f"{strings['client_address'].title()}:"
            f"{self.client.address:>{inv_len - 1 - len(strings['client_address'])}}"
        )
        print(
            f"{strings['iban'].title()}:"
            f"{self.client.iban:>{inv_len - 1 - len(strings['iban'])}.20}"
        )
        print(f"{datetime.now().strftime('%d-%m-%Y'):=^{inv_len}}")
        print()


client = Client("George Pascu", "Bucuresti", "RO76INGB00000000")
client1 = Client("Ion Pascu", "Iasi", "RO76INGB000000124300")

invoice1 = Invoice(client)
invoice2 = Invoice(client1)

invoice1.print_invoice("ro")
invoice2.print_invoice("en")