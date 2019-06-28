# Create your Character class logic in here.


class Character:

    was_guessed = False

    def __init__(self, char):
        if len(char) == 1 and (char.isalpha() or char == ' '):
            self.original = char
        else:
            print("Not a single letter character!")

    def guess_attempt(self, guess):
        if guess == self.original:
            self.was_guessed = True
            return self.was_guessed
        else:
            return False

    def show_character(self):
        if self.original == ' ':
            return ('  ')
        elif self.was_guessed:
            return(self.original)
        else:
            return '_'

