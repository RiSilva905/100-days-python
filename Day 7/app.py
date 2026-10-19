# Day 7 of 100

# Hangman game
import random
from hangman_words import word_lists
word_guess = []
lives = 6
choosen_word = random.choice(word_lists)
life = len(choosen_word)
#print(choosen_word) # For testing the word
for numbers in range (0,life):
    word_guess += "_"
print(word_guess)
end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess in choosen_word:
        for position in range(life):
            letter = choosen_word[position]
            if letter == guess:
                word_guess[position] = letter
    else:
        print("Wrong letter: " + str(guess))
        lives -= 1
        print("Remaining lives: " + str(lives))

    print(word_guess)

    if lives == 0:
        end_game = True
        print("You loose! Word was: " + str(choosen_word))
    
    if "_" not in word_guess:
        end_game = True
        print("You Win!")