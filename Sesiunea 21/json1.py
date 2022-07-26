import json
# JSON

# scriere
# direct in fisier
# json.dump()

# salvam intrun string
# json.dumps()

# citire
# din fisier direct
# json.load()

# conversie dintr-un string
# json.loads()

ticket = {
    "plecare": "OTP",
    "sosire": "TMS",
    "pret": 200,
    "loc": "3A",
    "ore": {
        "plecare": "19:39",
        "sosire": "20:30"
    }
}

ticket_json = json.dumps(ticket)

print(type(ticket))
print(type(ticket_json))
ticket_json = ticket_json[:-2]
print(ticket_json)


tk_from_json = json.loads(ticket_json)