class Pirate:
    def __init__(self, name):
        self.name = name

class Captain(Pirate):
    title = "Captain"
    rank = 10

class Quartermaster(Pirate):
    title = "Quartermaster"
    rank = 9

class Officer(Pirate):
    title = "Officer"
    rank = 7

class CannonOperator(Pirate):
    title = "Cannon Operator"
    rank = 6

class Cook(Pirate):
    title = "Cook"
    rank = 3

class DeckScrubber(Pirate):
    title = "Deck Scrubber"
    rank = 1
