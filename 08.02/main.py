from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll
from exchange import Bank

# loader = TestDataLoader()
loader = JSONDataLoader()

bank = Bank(loader)
payroll = Payroll()
missions = loader.load_missions()

for mission in missions:
    print(mission)
    ducats = bank.exchange(mission.loot)
    print(f"Loot exchanged for {ducats} Ducats.")
    shares = payroll.calculate_shares(mission.crew, ducats)
    for share in shares:
        print(share)
    print()
