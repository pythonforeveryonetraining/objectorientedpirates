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

pirates = [
    Captain("Harry"),
    Quartermaster("Isabel"),
    Officer("Bootstrap Bill"),
    CannonOperator("Powder Joe"),
    Officer("Four Finger Fritz"),
    CannonOperator("Lady Joyce")
]

ducats = 920
sum_of_ranks = sum(pirate.rank for pirate in pirates)

for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducats.")
