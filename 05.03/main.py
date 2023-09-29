from data import DataLoader
from data import JSONDataLoader

# loader = DataLoader()
loader = JSONDataLoader()
pirates = loader.load_pirates()

ducats = 1430
sum_of_ranks = sum(pirate.rank for pirate in pirates)

for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducats.")