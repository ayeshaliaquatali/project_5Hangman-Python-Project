# Hangman Python Project
# you will learn how to work with dictionaries, lists, and nested if statements. 
# You will also learn how to work with the 
# string and random Python modules.
import random

word_list = ["python","javascript","c++","tyescript","codidng","developer"]

chosen_word = random.choice(word_list)

words_length = len(chosen_word)

lives = 6 

display = ["_"] * words_length

guess_letter = set()

print("Welcome the Hangman!:")

while "_" in display and lives > 0 :
    guess = input("Guess the letter:")

    if guess in guess_letter:
        print("you have already guess the letter.Try again.")
        continue
    guess_letter.add(guess)
    if guess in chosen_word:
        for position in range(words_length):
            letter =  chosen_word[position] 
            if letter== guess:
                display[position]  = letter
        print("".join(display))
    else:
        lives -= 1
        print(f"Wrong guess: {guess}. You lost a life. Lives left: {lives}")
        #
        #print(f"The guessed {guess}")
        print("".join(display))


if "_" not in display:
    print("you win")
    print(f"The word was : {chosen_word}")
elif lives == 0:
    print("you lose")
    print(f"The word was : {chosen_word}") 
        