from GuessGame import num_o_pif
from MemoryGame import memory
from CurrencyRouletteGame import currency

def welcome(name):
    print("Hello " + name +"\n" +
    "Welcome to the World of Games (WoG). Here you can find many cool games to play.")

def check_my_input(choose, num):
    if choose.isnumeric() and int(choose) >= 1 and int(choose) <= num:
        return True
    else:
        return False


def load_game():
    print("Please choose a game to play: " + "\n" +
"1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"  + "\n" +
"2. Guess Game - guess a number and see if you chose like the computer" + "\n" +
"3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while True:
    #while true c'est une boucle qui tourne a l'infini
        game_choose = input("enter the game number you choose: ")
        if check_my_input(game_choose, 3):
            print("your choice of game number " + str(game_choose))
            choose_to_file = open("/Users/bennyronen/PycharmProjects/devops/WorldOfGames/choose_game.txt", "a")
            choose_to_file.write(game_choose)
            choose_to_file.close()

            while True:

                difficulty_choose = input("Please choose the difficulty of the game between 1 and 5: ")
                if check_my_input(difficulty_choose, 5):
                    print("the difficulty of your choice is " + str(difficulty_choose))
                    difficulty_to_file = open("/Users/bennyronen/PycharmProjects/devops/WorldOfGames/choose_of_gammer.txt",
                                             "a")
                    difficulty_to_file.write(difficulty_choose)
                    difficulty_to_file.close()

                    if game_choose == "2":
                        num_o_pif()
                        return
                    elif game_choose == "1":
                        memory()
                        return
                    elif game_choose == "3":
                        currency()
                        return

                else:
                    print("you did not choose a number between 1-5!")
        else:
            print("you did not choose a number between 1-3!")





