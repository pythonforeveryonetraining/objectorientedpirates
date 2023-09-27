from pirates import Pirate
from pirates import Role
import json

class DataLoader:
    def load_pirates(self):
        return [
            Captain("Harry"),
            Quartermaster("Isabel"),
            Officer("Bootstrap Bill"),
            CannonOperator("Powder Joe"),
            Officer("Four Finger Fritz"),
            CannonOperator("Lady Joyce"),
            Officer("Calypso"),
            CannonOperator("Moustache Mike")
        ]

class JSONDataLoader:
    def load_pirates(self):
        with open("data.json") as file:
            data = json.load(file)
        pirates = [Pirate(pirate["name"], Role(pirate["title"], pirate["rank"])) for pirate in data["pirates"]]
        return pirates
