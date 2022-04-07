from random_word import RandomWords
from art import stages, logo
import random

print(logo)
game=True
word=RandomWords()
chosen_word=word.get_random_word()
lives=6
already_guessed_letter=[]
displayed_word=[]
for i in range(len(chosen_word)):
    displayed_word.append("_")

print(f"The word has {len(chosen_word)} letters.")

while game:
	guess = input("Guess a letter: ").lower()

	if guess in already_guessed_letter:
		print("You already guessed this letter.")
	else:
	    for position in range(len(chosen_word)):
	        letter = chosen_word[position]
	        if letter == guess:
	            displayed_word[position] = letter

	if guess not in chosen_word:
		print(f"{guess} is not in the word.")
		lives-=1

	print(f"{' '.join(displayed_word)}")

	if "_" not in displayed_word:
		game = False
		print(f"The word is {chosen_word}")
		print("You win.")
	elif lives == 0:
		print(stages[lives])
		game = False
		print("You lose.")	
	else:
		print(stages[lives])