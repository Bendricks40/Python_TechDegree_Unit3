# Import your Game class
import copy
import masterPhraseList
from game import Game

phraselist = copy.deepcopy(masterPhraseList.fullList)

# Create your Dunder Main statement.
if __name__ == '__main__':
    myGame = Game(phraselist)
    myGame.start_game()


