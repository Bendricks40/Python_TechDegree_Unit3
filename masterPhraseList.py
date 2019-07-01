from phrase import Phrase


testList = ['a', 'bb']

fullList= ['A HOT POTATO',
'A PENNY FOR YOUR THOUGHTS',
'ACTIONS SPEAK LOUDER THAN WORDS',
'ADD INSULT TO INJURY',
'AT THE DROP OF A HAT']

bigPhraseList = []

for x in fullList:
    bigPhraseList.append(Phrase(x))
