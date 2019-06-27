# Import your Game class
from src import Game
import copy
from src import masterPhraseList


phraselist = copy.deepcopy(masterPhraseList.fullList)

# Create your Dunder Main statement.

if __name__ == '__main__':
    myGame = Game(phraselist)
    myGame.start_game()

