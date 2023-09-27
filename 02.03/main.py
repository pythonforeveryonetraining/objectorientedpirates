pirates = [
    ("Harry", "Captain", 10),
    ("Isabel", "Quartermaster", 9),
    ("Bootstrap Bill", "Mate", 7),
    ("Powder Joe", "Gunner", 6),
    ("Four Finger Fritz", "Mate", 7)
]
ducats = 850

sum_of_ranks = sum(rank for name, title, rank in pirates)

for name, title, rank in pirates:
    share = rank / sum_of_ranks * ducats
    print(f"{title} {name} gets {share:.2f} Ducats.")
