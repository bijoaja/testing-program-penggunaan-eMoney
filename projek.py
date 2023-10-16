'''
Public Transport Program Using E-Money 
'''

class EMoneyCard:
    def __init__(self, name="", balance=0):
        self.name = name
        self.balance = balance
    
    def getName(self):
        return self.name
    
    def check_balance(self):
        balance = f"{self.balance:,}"
        return balance
    
    def top_up(self, amount):
        self.balance += amount
        return f"Top-up successful. Current balance: {self.balance:,}"
        
    def deduct(self, fare):
        if self.balance >= fare:
            self.balance -= fare
            return f"Payment successful. Remaining balance: {self.balance:,}"
        else:
            return "Insufficient balance. Please top-up your card."
    
class Halte:
    def __init__(self, startHalte="", finishHalte="", transportation=""):
        self.halte = {"Cikampek":1, "Bogor":2, "Depok":3, "Bekasi":4, "Jakarta":5}
        self.kelas = {"Ekonomi": 2000, "Eksekutif": 3000, "Bisnis": 4000}
        self.transportation = transportation
        self.startHalte = self.halte[startHalte]
        self.finishHalte = self.halte[finishHalte]
        self.cost = 0
    
    def getCostLines(self):
        return abs(self.startHalte-self.finishHalte)*2000
    
    def getCostTransportation(self):
        return self.kelas[self.transportation]
    
    def getCost(self):
        return self.cost
    
    def totalCost(self):
        self.cost = self.getCostLines() + self.getCostTransportation()