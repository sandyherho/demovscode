import math
import sys
from os import rename

import requests

print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://herhoresume.herokuapp.com")
print(r.status_code)

name = input("your name? ")
print("hello ", name)
