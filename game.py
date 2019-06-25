# Create your Game class logic in here.
import random
from Projectfiles.phrase import Phrase
from Projectfiles.character import Character



phraselist = ['A hot potato',
              'A penny for your thoughts',
              'Actions speak louder than words',
              'Add insult to injury',
              'At the drop of a hat',
              'Back to the drawing board',
              'Ball is in your court',
              'Barking up the wrong tree',
              'Be glad to see the back of',
              'Beat around the bush',
              'Best of both worlds',
              'Best thing since sliced bread',
              'Bite off more than you can chew',
              'Blessing in disguise',
              'Burn the midnight oil',
              'Cant judge a book by its cover',
              'Caught between two stools',
              'Costs an arm and a leg',
              'Cross that bridge when you come to it',
              'Cry over spilt milk',
              'Curiosity killed the cat',
              'Cut corners',
              'Cut the mustard',
              'Devils Advocate',
              'Dont count your chickens before the eggs have hatched',
              'Dont give up the day job',
              'Dont put all your eggs in one basket',
              'Drastic times call for drastic measures',
              'Elvis has left the building',
              'Every cloud has a silver lining',
              'Far cry from',
              'Feel a bit under the weather',
              'Give the benefit of the doubt',
              'Hear it on the grapevine',
              'Hit the nail on the head',
              'Hit the sack',
              'In the heat of the moment',
              'It takes two to tango',
              'Jump on the bandwagon',
              'Keep something at bay',
              'Kill two birds with one stone',
              'Last straw',
              'Let sleeping dogs lie',
              'Let the cat out of the bag',
              'Make a long story short',
              'Method to my madness',
              'Miss the boat',
              'Not a spark of decency',
              'Not playing with a full deck',
              'Off ones rocker',
              'On the ball',
              'Once in a blue moon',
              'Picture paints a thousand words',
              'Piece of cake',
              'Put wool over other peoples eyes',
              'See eye to eye',
              'Sit on the fence',
              'Speak of the devil',
              'Steal someones thunder',
              'Take with a grain of salt',
              'Taste of your own medicine',
              'To hear something straight from the horses mouth',
              'Whole nine yards',
              'Wouldnt be caught dead',
              'Your guess is as good as mine']


class Game:

    activePhrase = "blah"

    def __init__(self, phrases):
        self.phrases = phrases
        self.activePhrase = self.phrases[random.randint(1, len(self.phrases))].upper()

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
            print(currentPhrase.incorrect_guesses)

            # Display the remaining phrase after running their last guess:
            print(currentPhrase.display_phrase())

        if currentPhrase.phrase_guessed_status():
            print("\n\nCongratulations!! You have guessed correctly.\n\n")

myGame = Game(phraselist)
myGame.start_game()

