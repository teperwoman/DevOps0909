import random

def memory():
    difficulty_to_file = open("/Users/bennyronen/PycharmProjects/devops/WorldOfGames/choose_of_gammer.txt", "r")
    content = difficulty_to_file.read()
    difficulty_to_file.close()

    list_number_ramdom = random.sample(range(1,101), int(content))


    while True:

        n = int(content)
        list_number_choose_gammer = list(map(int, input("enter " + str(content) + " digits between 1 - 101, separated by comma: ").strip().split(",")))[:n]

        if list_number_ramdom == list_number_choose_gammer:
            print(True)
            return
        else:
            print(False)





