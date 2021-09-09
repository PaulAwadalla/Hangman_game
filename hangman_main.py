import random
import hangman_words
import hangman_UI
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
os.system('clear')
print(hangman_UI.logo)
print("-----------------------------------------------\n")
print("You have '6' lives to guess the word. Good luck!")
print("\n")
print(f'Pssst, the solution is {chosen_word}.')
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    if guess in display:
        print(f"the letter '{guess}' you have already guessed before.")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"the letter '{guess}' you have guessed is not in this word")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print("\n")
    print(hangman_UI.stages[lives])
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("-------------------")
        print("YOU WIN!!!!")
        print("-------------------\n")

    if lives == 0:
        end_of_game = True
        print("uh oh! YOU LOSE!")
        print("-------------------")
        print(f'Pssst, the solution is {chosen_word}.')
        print("-------------------\n")
