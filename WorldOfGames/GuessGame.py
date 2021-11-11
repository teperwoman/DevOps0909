import random

def num_o_pif():
    difficulty_to_file = open("/Users/bennyronen/PycharmProjects/devops/WorldOfGames/choose_of_gammer.txt", "r")
    content = difficulty_to_file.read()
    difficulty_to_file.close()
    mistery_num = random.randint(1, int(content))

    while True:
        get_guess_from_user = input("guess what is the number?")
        if int(get_guess_from_user) == mistery_num:
            print("Well done this is a correct guess!")
            return
        else:
            print("Oh no, that's not a correct guess!")
