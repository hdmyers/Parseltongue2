import random
import os
import time

categories = ["Heath", "Algebra", "Mario", "Fantasy", "Worm", "Nasuverse"]

def play_game():
    start_time = time.time()
    chosen_category = categories[random.randint(0, len(categories)-1)]
    print("Your category is: " + chosen_category)
    answers = list()

    while len(answers)<10:
        new_answer = input("\nWhat thing are you think of that falls under the category of " + chosen_category + "?")
        if new_answer in answers or new_answer.replace(" ", "") == "":
            print("That's a bad answer!")
        else:
            answers.append(new_answer)
            print("\nYour answers are: ")
            for answer in answers:
                print(answer.center(os.get_terminal_size().columns))

    print("\nIt took you " + str(time.time() - start_time) + " seconds to complete the game!")

play_game()
