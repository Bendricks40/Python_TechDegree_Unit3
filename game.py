# Create your Game class logic in here.
import copy
import random
import masterPhraseList


class Game:

    def __init__(self, phraseList):
        self.phraseList = phraseList
        self.activePhrase = self.phraseList[random.randint(0, len(self.phraseList)-1)]
        self.gameOver = False
        self.remainingLives = 5
        print("just initialized game!")
        print(self.activePhrase.display_phrase())
        print(self.activePhrase.)

    def start_game(self):

        print("\n**********************************************"
              "\n****** Welcome to Phrase Hunter! *************"
              "\n**********************************************\n")
        print("Try to guess the idiom before you run out of attempts. "
              "You are allowed 5 misses before you lose the game!\n")
        phraselist = copy.deepcopy(masterPhraseList.bigPhraseList)
        currentPhrase = self.activePhrase
        print("Below is your phrase to guess - you have {} lives remaining:".format(self.remainingLives))
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
            elif currentPhrase.guess_attempt(guess):
                print("NICE!! {} is part of the idiom".format(guess))
            else:
                print("YIKES! {} is not in the idiom. You have lost a life. ".format(guess))
                self.remainingLives -= 1

            # if the user's guess is wrong, decrement their remaining lives:
            if self.remainingLives < 1:

                if input("\n\nYou have lost!! Play again? enter 'Y' for new game: ").upper() == 'Y':
                    self.activePhrase = ''
                    newGame = Game(phraselist)
                    newGame.start_game()
                else:
                    print("\n\nHope you enjoyed the game, thanks for playing! Have a great day! \n\n")
                    exit()


            if not self.gameOver:
                print("Remaining Lives: {}\n".format(self.remainingLives))
                print(currentPhrase.display_phrase())
            if currentPhrase.phrase_guessed_status():
                print("\n\nCongratulations!! You have guessed correctly with {} lives remaining!\n\n".format(self.remainingLives))
                response = input("Play again? enter 'Y' for new game: ").upper()
                if response == 'Y':
                    self.activePhrase = ''
                    newGame = Game(phraselist)
                    newGame.start_game()
                else:
                    print("\n\nHope you enjoyed the game, thanks for playing! Have a great day! \n\n")
                    exit()
