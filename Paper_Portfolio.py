#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Portfolio:
    
    def __init__(self, initial_balance, leverage=1):
        self.balance = initial_balance
        self.position = 0  
        self.trade_log = []
        self.entry_price = None
        self.entry_volume = None
        self.leverage = leverage
    
    def enter_long(self, price, volume):
        max_volume = (self.balance * self.leverage) / price
        volume = min(volume, max_volume)  # You can't buy more than your leveraged balance allows
        self.entry_price = price
        self.entry_volume = volume
        self.balance -= price * volume
        self.position += volume
        self.trade_log.append(("LONG", price, volume))

    def exit_long(self, price, volume):
        volume = min(volume, self.position)  # You can't sell more than you own
        profit = (price - self.entry_price) * volume
        self.entry_price = None
        self.entry_volume = None
        self.balance += price * volume
        self.position -= volume
        self.trade_log.append(("EXIT LONG", price, volume, profit))

    def enter_short(self, price, volume):
        max_volume = (self.balance * self.leverage) / price
        volume = min(volume, max_volume)
        self.entry_price = price
        self.entry_volume = volume
        self.balance += price * volume
        self.position -= volume
        self.trade_log.append(("SHORT", price, volume))

    def exit_short(self, price, volume):
        volume = min(volume, abs(self.position))  # You can't cover more than you shorted
        profit = (self.entry_price - price) * volume
        self.entry_price = None
        self.entry_volume = None
        self.balance -= price * volume
        self.position += volume
        self.trade_log.append(("EXIT SHORT", price, volume, profit))

    def calculate_profit(self):
        return sum([trade[3] for trade in self.trade_log if len(trade) == 4])

