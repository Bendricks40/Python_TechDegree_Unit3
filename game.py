# Create your Game class logic in here.
import random
import copy
import masterPhraseList
from phrase import Phrase

phraselist = copy.deepcopy(masterPhraseList.fullList)


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
        print("Try to guess the idiom before you run out of attempts. You are allowed 5 misses before you lose the game!\n")
        currentPhrase = Phrase(self.activePhrase)
        print("Below is your phrase to guess - you have {} lives remaining:".format(currentPhrase.remaining_lives))
        print(currentPhrase.display_phrase())

        guess = ''
        # While user has not input valid guess and entire phrase has NOT already been guessed, prompt for another guess:
        while (len(guess) > 1) or (not guess.isalpha()) or (not currentPhrase.phrase_guessed_status()):
            guess = input("\nEnter a letter: \n").upper()
            if len(guess)>1:
                print("\nEnter just one character, please!")
            elif guess in currentPhrase.alreadyGuessed:
                print("Oops! You have already guessed {}. Try again.".format(guess))
            elif not guess.isalpha():
                print("That was not a letter--try again!")
            else:
                # Take the user's guess and see if it is valid:
                currentPhrase.guess_attempt(guess)

            # if the user's guess is wrong, decrement their remaining lives:
            if currentPhrase.remaining_lives < 1:

                if input("You have lost!! Play again? enter 'Y' for new game").upper() == 'Y':
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
                response = input("Play again? enter 'Y' for new game: ").upper()
                if response == 'Y':
                    self.activePhrase = ''
                    newGame = Game(phraselist)
                    newGame.start_game()
                else:
                    print("Thanks for playing!!\n\n")
                    break




