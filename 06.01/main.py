from data import DataLoader
from data import JSONDataLoader

# loader = DataLoader()
loader = JSONDataLoader()
pirates = loader.load_pirates()

ducats = 1610
sum_of_ranks = sum(pirate.role.rank for pirate in pirates)

for pirate in pirates:
    share = pirate.role.rank / sum_of_ranks * ducats
    print(f"{pirate.role.title} {pirate.name} gets {share:.2f} Ducats.")
