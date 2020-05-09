import requests
import matplotlib

r = requests.get("https://herhoresume.herokuapp.com")
print(r.status_code)

name = input("your name? ")
print("hello ", name)
