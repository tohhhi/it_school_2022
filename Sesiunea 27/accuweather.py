# 1. Cere nume de localitate de la tastatura.

import requests
import json



key = []

def city():
    city_name = input("Type a city name:")
    try:
        # 1. Facem requests
        response = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=PTTdz96fPpcNgmEx0jf5560TsYEiqOK6&q={city_name}")
    except requests.exceptions.RequestException as err:
        print(err)
    else:
        # 2. Verificam status code sa fie 200
        if response.status_code == 200:
            # 3. Extragem datele
            data = response.json()

            

            for i in data:
                key.append(i["Key"])

            



def city_conditions():
    id = key[0]
    
    try:
        # 1. Facem requests
        response = requests.get(f"http://dataservice.accuweather.com/currentconditions/v1/{id}?apikey=PTTdz96fPpcNgmEx0jf5560TsYEiqOK6")
    except requests.exceptions.RequestException as err:
        print(err)
    else:
        # 2. Verificam status code sa fie 200
        if response.status_code == 200:
            # 3. Extragem datele
            data = response.json()

            for i in data:
                print(i["Temperature"])



city()
city_conditions()




