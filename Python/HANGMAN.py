# HI, Today I am building The Hangman Game.     Date: 25/6/23
import random

# START

print("Hey, you have been given a 'do or die' task.")
input("Press Enter Key to Continue")
print("Find the correct word and save the innocent man from getting hanged!")
input("Press Enter Key to Continue")
print("Let's Begin!!")


word_list= ["HYDROGEN", "HELIUM", "LITHIUM", "BERYLLIUM", "BORON", "CARBON", "NITROGEN", "OXYGEN", "FLUORINE", "NEON"]
# MISTAKE: Always put the words in set in quotations or the terminal wont read it as a string and show us error as so and so thing is undefined etc.

word = random.choice(word_list)

chances = 8
guessed_word = "-" * len(word)
print(guessed_word)


while chances > 0:
    letter = input("Guess a letter: ").upper()
#MISTAKE : always check if the variables are correctly placed and used in the lopps and if else statements.
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[ : index] + letter + guessed_word[index+1 :]
        print(guessed_word)

        if guessed_word == word:
            print("Congratulations! You saved the innocent man!")
            break
    else:
        chances -= 1
        print("Wrong letter! Chances remaining:", chances)


if chances == 0:
    print("Game Over! The correct answer was: ", word)



