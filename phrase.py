# Create your Phrase class logic here.
from Projectfiles.character import Character


class Phrase:

    phrase = ''
    rawCharacters = []
    CharacterObjectList = []
    displayed_phrase = ''
    guessed = False
    incorrect_guesses = 0

    def __init__(self, phrase):
        self.phrase = phrase
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
        for x in self.CharacterObjectList:
            x.guess_attempt(guess)
            if x.guess_attempt:
                guess_status = True
            else:
                self.incorrect_guesses += 1
        return guess_status

