from pirates import Captain
from pirates import Quartermaster
from pirates import Officer
from pirates import CannonOperator

class DataLoader:
    def load_pirates(self):
        return [
            Captain("Harry"),
            Quartermaster("Isabel"),
            Officer("Bootstrap Bill"),
            CannonOperator("Powder Joe"),
            Officer("Four Finger Fritz"),
            CannonOperator("Lady Joyce")
        ]
