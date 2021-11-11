import requests
import random

def currency():
    difficulty_to_file = open("/Users/bennyronen/PycharmProjects/devops/WorldOfGames/choose_of_gammer.txt", "r")
    diff = difficulty_to_file.read()
    difficulty_to_file.close()

    d = int(diff)

    url = 'https://v6.exchangerate-api.com/v6/d71c5b38681bf2b7fc53aeab/latest/USD'

    response = requests.get(url)
    data = response.json()

    usd_money = (data['conversion_rates']['USD'])
    ils_money = (data['conversion_rates']['ILS'])

    random_num = random.randint(1, 100)

    t = int(usd_money * random_num)
    ils_usd = int(t * ils_money)

    print(str(ils_usd) + " ils_usd")

    marge = 5 - int(d)
    mar_min = (t - marge)
    mar_max = (t + marge)

    while True:
        get_guess_from_user = input("enter a guess of value to a amount of " +  str(t)  + " USD in ILS: ")
        if int(get_guess_from_user) == ils_usd:
            print(True)
            return
        elif int(get_guess_from_user) >= mar_min:
            print(True)
            return
        elif int(get_guess_from_user) <= mar_max:
            print(True)
            return
        else:
            print(False)

