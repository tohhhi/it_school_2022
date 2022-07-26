from urllib import response
import requests


response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")


print(response)