# Create your Game class logic in here.
import random
from Projectfiles.phrase import Phrase
from Projectfiles.character import Character



phraselist = ['A hot potato','A hot potato']


class Game:

    activePhrase = "blah"

    def __init__(self, phrases):
        self.phrases = phrases
        self.activePhrase = self.phrases[random.randint(1, len(self.phrases)-1)].upper()

    def start_game(self):

        print("\n**********************************************"
              "\n****** Welcome to Phrase Hunter! *************"
              "\n**********************************************\n")
        print("Try to guess the idiom before you run out of attempts.\n")
        print("Below is your first phrase to guess:")
        currentPhrase = Phrase(self.activePhrase)
        print(currentPhrase.display_phrase())

        guess = ''
        # While user has not input valid guess and entire phrase has NOT already been guessed, prompt for another guess:
        while (len(guess) > 1) or (not guess.isalpha()) or (not currentPhrase.phrase_guessed_status()):
            guess = input("\nEnter a letter: \n").upper()
            if len(guess)>1:
                print("\nEnter just one character, please!")
            if not guess.isalpha():
                print("That was not a letter--try again!")

            # Take the user's guess and see if it is valid:
            currentPhrase.guess_attempt(guess)

            #if the user's guess is wrong, decrement their remaining lives:
            print("Remaining Lives: {}".format(currentPhrase.remaining_lives))

            # Display the remaining phrase after running their last guess:
            print(currentPhrase.display_phrase())

        if currentPhrase.phrase_guessed_status():
            print("\n\nCongratulations!! You have guessed correctly.\n\n")

myGame = Game(phraselist)
myGame.start_game()

