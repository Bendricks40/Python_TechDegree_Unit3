# Create your Phrase class logic here.
from Projectfiles.character import Character


class Phrase:

    phrase = ''
    rawCharacters = []
    CharacterObjectList = []
    displayed_phrase = ''
    guessed = False

    def __init__(self, phrase):
        self.phrase = phrase
        self.rawCharacters = list(phrase)
        for char in self.rawCharacters:
            self.CharacterObjectList.append(Character(char))

    def display_phrase(self):
        self.displayed_phrase = ''
        for x in self.CharacterObjectList:
            self.displayed_phrase += (' ' + x.show_character())
        print(self.displayed_phrase)

    def guessed_status(self):
        if '_' in self.displayed_phrase:
            return False
        else:
            return True

    def guess_attempt(self, guess):
        for x in self.CharacterObjectList:
            x.guess_attempt(guess)

