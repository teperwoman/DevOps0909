from datetime import datetime
import requests
from time import sleep


while True:
    response = requests.get("https://github.com")
    if response.status_code != 200:
        print("gitgub is down")
    else:
        print("github is still ok")
    sleep(5)
