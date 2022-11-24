#Wordle Solver
#copyright 2022 Rebecca Schwab

import random
import time

a = 2
b = 3
c = 4
d = 5

# This code imports the word lists

with open(r"C:\Users\Rebecca\Desktop\Wordle Solver\answers.txt") as answers_file:
  wordle_answers = answers_file.read().split()

with open(r"C:\Users\Rebecca\Desktop\Wordle Solver\allowed.txt") as allowed_file:
    allowed_guesses = allowed_file.read().split()

# This code combines the two word lists and shuffles them so the answers list is mixed in with the allowed guesss list
full_word_list = allowed_guesses + wordle_answers
full_list_shuffled = random.sample(full_word_list, len(full_word_list))

# The next set of variables are where you will manually enter what you know so far. 

known_letters = []

# Enter any letters you've eliminated below. 

eliminated = []

# This code lets you enter the positions of the letters you know.

known_position = []

# This code accepts the *incorrect* positions of the letters you know

wrong_position = []
 
# This is the function that does the work

def solve_wordle():
    possible_words = set()
    for word in full_list_shuffled:
        has_eliminated = any([letter in word for letter in eliminated])
        if not has_eliminated:
            has_known = all([known in word for known in known_letters])
            if has_known:
                if known_position:
                    has_known_position = all([(word[pair[0]] == pair[1]) for pair in known_position])
                    if has_known_position:
                        has_wrong_position = any([(word[pair[0]] == pair[1]) for pair in wrong_position])
                        if not has_wrong_position:
                            possible_words.add(word)
                elif wrong_position:
                    has_wrong_position = any([(word[pair[0]] == pair[1]) for pair in wrong_position])
                    if not has_wrong_position:
                        possible_words.add(word)
                else:
                    possible_words.add(word)
    print(possible_words)                       

           
#solve_wordle()

#Adding an intro for the user

def intro():
    print("")
    print("")
    print("Welcome to my Wordle Solver!")
    print("")
    time.sleep(a)
    while True:
        print("")
        need_intro = input("Do you want me to play the intro? Y/N: ")
        if need_intro.lower() not in ("y", "n"):
            print("")
            time.sleep(a)
            print("I'm sorry, I didn't understand that.")
            print("")
            time.sleep(a)
            print("Please answer 'Y' or 'N'")
            time.sleep(a)
        else:
            break
    if need_intro.lower() == "n":
            print("")
            time.sleep(a)
            print("Ok, we'll get right to it then!")
            print("")
            time.sleep(a)
            get_eliminated()
    else:
        print("")
        print("This program assumes you're familiar with how to play Wordle")
        time.sleep(b)
        print("and that you've come here for help when you *just can't think* of a 5-letter word")
        time.sleep(c)
        print("that fits the letters you know and the ones you've eliminated.")
        time.sleep(c)
        print("")
        print("First, I'm going to ask you to enter any letters you've completely eliminated from the word.")
        time.sleep(c)
        print("Then, I'm going to ask you about the letters you know are in the word.")
        time.sleep(c)
        print("I'm going to ask you for the letter itself, and any correct or incorrect positions of the letter in the word.")
        time.sleep(d)
        print("")
        print("Once I have that information, I'll show you a list of all the 5-letter words that fit the criteria you've given me.")
        time.sleep(d)
        print("")
        print("It will be important that you follow my instructions exactly")
        time.sleep(c)
        print("or my program may not give you the correct answer(s).")
        time.sleep(c)
    
        while True:
            print("")
            time.sleep(a)
            get_started = input("Are you ready to get started? Y/N: ")
            if get_started.lower() not in ("y", "n"):
                print("")
                time.sleep(a)
                print("I'm sorry, I didn't understand that.")
                print("")
                time.sleep(a)
                print("Please answer 'Y' or 'N'")
                time.sleep(a)
            else:
                break
        if get_started.lower() == "y":
            print("")
            time.sleep(a)
            print("Ok, great! Here we go!")
            print("")
            time.sleep(a)
            get_eliminated()
        else:
            print("")
            time.sleep(a)
            print("No worries. Please come back when you're ready.")
            print("")
            time.sleep(a)

# This function lets you input the eliminated letters
def get_eliminated():
    print("First, let's address any letters you've eliminated.")
    while True:
        print("")
        time.sleep(a)
        any_eliminated = input("Have you eliminated any letters from the word? Y/N: ")
        if any_eliminated not in ("y", "n"):
            print("")
            time.sleep(a)
            print("I'm sorry, I didn't understand that.")
            print("")
            time.sleep(a)
            print("Please answer 'Y' or 'N'")
            time.sleep(a)
        else:
            break
    if any_eliminated == "y":
            print("")
            time.sleep(a)
            print("Ok, let's have you enter those letters now.")
            print("")
            time.sleep(a)
            print("Pleae type in the letters with a space in between each one in this format:")
            print("")
            time.sleep(a)
            print("a b c d e ")
            print("")
            time.sleep(a)
            print("If you enter the letters incorrectly, I won't be able to give you the right answers.")
            print("")
            time.sleep(a)
            while True:
                enter_eliminated = input("Enter the eliminated letters now: ")
                if not enter_eliminated:
                    print("")
                    time.sleep(a)
                    print("I'm sorry, you didn't enter any info.")
                    print("")
                    time.sleep(a)
                else:
                    break
            print(enter_eliminated)
            for letter in enter_eliminated.split():
                eliminated.append(letter)
                print(eliminated)
            print("")
            time.sleep(a)
            print("Thank you. Now, let's talk about any letters you know.")

    else:
        print("")
        time.sleep(a)
        print("Ok, we'll move on then.")
        print("")
        time.sleep(a)

#get_eliminated()
intro()