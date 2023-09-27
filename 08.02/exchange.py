class Currency:
    def __init__(self, name, exchange_rate):
        self.name = name
        self.exchange_rate = exchange_rate

    def value_in_ducats(self, amount):
        return amount * self.exchange_rate
    
class Bank:
    def __init__(self, loader):
        self.loader = loader

    def exchange(self, loot):
        currencies = self.loader.load_currencies()
        total_ducats = 0
        for loot_item in loot:
            currency = currencies[loot_item.currency_key]
            ducats = currency.value_in_ducats(loot_item.amount)
            total_ducats = total_ducats + ducats
        return total_ducats