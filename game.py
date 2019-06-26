# Create your Game class logic in here.
import random
import copy
from Projectfiles import masterPhraseList
from Projectfiles.phrase import Phrase

phraselist = copy.deepcopy(masterPhraseList.testList)


class Game:

    activePhrase = "blah"
    phrases = []

    def __init__(self, phrases):
        self.phrases = phrases
        self.activePhrase = self.phrases[random.randint(0, len(self.phrases)-1)].upper()

    def start_game(self):

        print("\n**********************************************"
              "\n****** Welcome to Phrase Hunter! *************"
              "\n**********************************************\n")
        print("Try to guess the idiom before you run out of attempts.\n")
        currentPhrase = Phrase(self.activePhrase)
        print("Below is your phrase to guess - you have {} lives:".format(currentPhrase.remaining_lives))
        print(currentPhrase.display_phrase())

        guess = ''
        # While user has not input valid guess and entire phrase has NOT already been guessed, prompt for another guess:
        while (len(guess) > 1) or (not guess.isalpha()) or (not currentPhrase.phrase_guessed_status()):
            if currentPhrase.phrase_guessed_status():
                print("\n\nCongratulations!! You have guessed correctly and are somehow back in the loop?????.\n\n")

            guess = input("\nEnter a letter: \n").upper()
            if len(guess)>1:
                print("\nEnter just one character, please!")
            if not guess.isalpha():
                print("That was not a letter--try again!")

            # Take the user's guess and see if it is valid:
            currentPhrase.guess_attempt(guess)

            # if the user's guess is wrong, decrement their remaining lives:
            if currentPhrase.remaining_lives < 1:

                if input("You have lost!! Play again? enter 'Y' for new game")=='Y':
                    self.activePhrase = ''
                    newGame = Game(phraselist)
                    newGame.start_game()
                else:
                    break
            print("Remaining Lives: {}\n".format(currentPhrase.remaining_lives))

            # Display the remaining phrase after running their last guess:
            print(currentPhrase.display_phrase())
            if currentPhrase.phrase_guessed_status():
                print("\n\nCongratulations!! You have guessed correctly with {} lives remaining!\n\n".format(currentPhrase.remaining_lives))
                if input("Play again? enter 'Y' for new game") == 'Y':
                    self.activePhrase = ''
                    newGame = Game(phraselist)
                    newGame.start_game()
                else:
                    break


myGame = Game(phraselist)
myGame.start_game()

