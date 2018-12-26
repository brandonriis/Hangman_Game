
# Hangman Game

import random


def main():

    print("Welcome to Hangman!")
    print("You have 10 goes to guess a randomly selected word!")
    print("Can you do it!?\n")

    game()


def game():

    word = randomword()

    word_list = []
    for i in range(len(word)):
        word_list.append("_")

    print(f"\n\nYour word is {len(word)} letters long! Good luck!")

    for i in range(len(word)):
        print(word_list[i], end=" ")

    counter = 0

    while(counter < 10):

        print(f"\n\nYou have {10 - counter} tries left.")

        while True:
            choice = input("\nPlease guess a letter: ")

            if(len(choice) == 1):
                pass
            else:
                print("Please enter only one character!")
                continue

            if (choice.isalpha()) == True:
                break
            else:
                print("\nPlease enter a character from A - Z!")
                continue


        if choice in word:
            print("\nGood guess, you letter has been added below in the correct place!")
            char_pos = charposition(word, choice)
            addchar(choice,word_list, char_pos)
            counter = counter + 1
            check = checkwin(word_list)
            if (check == True):
                break
            else:
                continue
        else:
            print("\nSorry you made the wrong choice! Try again!")
            counter = counter + 1
            for i in range(len(word)):
                print(word_list[i], end=" ")

    if check == True:
        print("\n\nWell done!! You guessed the correct word!")
    else:
        print(f"\n\nSorry you have run out of tries! The word was - {word} -")

    again = input("\nWould you like to play again? Y/N: ").upper()

    while (again != "Y" and again != "N"):
        print("\nPlease enter Y or N!")
        again = input("\nWould you like to play again? Y/N: ").upper()

    if(again == "Y"):
        game()
    else:
        exit()


def randomword():
    # Choose random word from "Words.txt" file
    text = open("Words.txt", "r").read().splitlines()
    word = random.choice(text)

    # Test print
    # print(word)

    return(word)


def charposition(string, char):

    pos = []
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


def addchar(char,word_list, char_pos):
    for i in range(len(char_pos)):
        word_list[char_pos[i]] = char

    print("")

    for i in range(len(word_list)):
        print(word_list[i], end=" ")


def checkwin(char_list):

    if ("_" not in char_list):
        return True
    else:
        return False


main()
