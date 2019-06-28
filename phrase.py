# Create your Phrase class logic here.
from character import Character


class Phrase:

    displayed_phrase = ''

    def __init__(self, phrase):
        self.CharacterObjectList = []
        self.alreadyGuessed = []
        self.phrase = phrase
        self.guessed = False
        self.rawCharacters = list(phrase)
        for char in self.rawCharacters:
            self.CharacterObjectList.append(Character(char))

    def display_phrase(self):
        self.displayed_phrase = ''
        for x in self.CharacterObjectList:
            self.displayed_phrase += (' ' + x.show_character())
        return self.displayed_phrase

    def phrase_guessed_status(self):
        if '_' in self.displayed_phrase:
            return False
        else:
            return True

    def guess_attempt(self, guess):
        guess_status = False
        self.alreadyGuessed.append(guess)
        for x in self.CharacterObjectList:
            if x.guess_attempt(guess):
                guess_status = True
        return guess_status

