from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll

loader = TestDataLoader()
# loader = JSONDataLoader()

payroll = Payroll()
missions = loader.load_missions()

for mission in missions:
    print(mission)
    shares = payroll.calculate_shares(mission.crew, mission.loot)
    for share in shares:
        print(share)
    print()
