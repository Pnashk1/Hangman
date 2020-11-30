import random
from Hangman_art import stages, logo #imported Hangman images from personally created module
from Hangman_words import word_list #imported Hangman word list from personally created module

TestSeed=input('Type a number please?')

random.seed(TestSeed) #seed set to get the same chosen_word

print(logo)
game_is_finished = False
lives = len(stages) - 1
guess_incorrect=[]

chosen_word = random.choice(word_list)
chosen_word
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_" #setting the blank spaces to the same length as the random word

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
        continue #if guess guessed is in disiplay skip over it

    if guess in guess_incorrect:
        print(f"You've already guessed {guess}")
        continue #if guess guessed is in the incorrect list skip over it

    for position in range(word_length):
        letter = chosen_word[position] #chosen_word elements are looped to and assigned to letter variable
        if letter == guess:
            display[position] = letter #display position is assigned letter variable if guess is correct
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        guess_incorrect.append(guess)
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1 #live decrease by 1 for every incorrect guess
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
