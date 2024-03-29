import requests
import json

try:
    # 1. Facem requests
    response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
except requests.exceptions.RequestException as err:
    print(err)
else:
    # 2. Verificam status code sa fie 200
    if response.status_code == 200:
        # 3. Extragem datele
        # data = json.loads(response.content)
        data = response.json()
        print(data)
    else:
        print(response.content)