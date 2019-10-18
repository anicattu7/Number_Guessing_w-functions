import datetime
import json
import random


#####################################################

def play_game():
    attempts = 0
    name = input("Enter your name: \n")

    while True:
        user_guess = int(input("Enter your guess between 1 and 30: \n"))
        attempts += 1

        if user_guess == sec_num:
            print("You got it right!!! {0} is the secret number".format(sec_num))

            new_list = {"name": name,
                        "attempts": attempts,
                        "date": str(datetime.datetime.now()),
                        "secret_num": sec_num,
                        "wrong_guesses": wrong_guesses}
            score_list.append(new_list)
            with open("score.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))


            break

        elif user_guess < sec_num:
            print("Think higher")

        elif user_guess > sec_num:
            print("Think lower")

        wrong_guesses.append(user_guess)

###########################################################################

def get_score_list():
    for list in score_list:
        print("Player {0} got secret number: {1} guessed correct in "
              "{2} attempts on {3} and the wrong guesses were {4}".format(list.get("name"),
                                                                          str(list.get("secret_num")),
                                                                          list.get("attempts"),
                                                                          str(list.get("date")),
                                                                          str(list.get("wrong_guesses"))))

###########################################################################


def get_top_scores():
    sort = sorted(score_list, key = lambda i: i["attempts"])[:3]
    for x in sort:
        print(x)


###########################################################################

score_list = []
wrong_guesses = []
sec_num = random.randint(1, 30)
attempts = 0

with open("score.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    #print(str(score_list))


while True:
    select = input("Enter your selection:- \n A-- Play a new game \n B-- Get the score list \n C-- Get the top scores  \n").upper()

    if select == "A":
        play_game()
        break
    elif select == "B":
        get_score_list()
        break
    elif select == "C":
        get_top_scores()
        break
