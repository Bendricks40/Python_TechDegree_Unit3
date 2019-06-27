# Import your Game class
from Projectfiles.game import Game
from Projectfiles import masterPhraseList
from Projectfiles.phrase import Phrase
import copy

phraselist = copy.deepcopy(masterPhraseList.fullList)


# Create your Dunder Main statement.

if __name__ == '__main__':
    myGame = Game(phraselist)
    myGame.start_game()

