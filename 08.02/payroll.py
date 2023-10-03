class Share:
    def __init__(self, pirate, ducats):
        self.pirate = pirate
        self.ducats = ducats
        
    def __str__(self):
        return f"{self.pirate.role.title} {self.pirate.name}, rank {self.pirate.role.rank} gets share {self.ducats:.2f} Ducats."

class Payroll:
    def calculate_shares(self, crew, ducats):
        sum_of_ranks = sum(pirate.role.rank for pirate in crew)
        return [Share(pirate, pirate.role.rank / sum_of_ranks * ducats) for pirate in crew]