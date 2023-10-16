'''
Public Transport Program Using E-Money 
'''

from projek import *

def destination():
    halte = ["Cikampek", "Bogor", "Depok", "Bekasi", "Jakarta"]
    transportation = ["Ekonomi", "Eksekutif", "Bisnis"]
    label = ["start", "finish", "transportation"]
    result = []
    for i in label:
        print('='*35)
        print('Welcome to Amazing Bus')
        print(f'Choose your {i} destination: ')
        if i != "transportation":
            for index,destination in enumerate(halte):
                print(str(index+1)+'.',f'{destination} \t')
            choose = int(input("Select by Number: "))
            if choose not in [i for i in range(1,len(halte)+1)]:
                raise "ERROR INPUT PLEASE RELOG"
            result.append(halte[choose-1])
            del halte[choose-1]
        else:
            for index,destination in enumerate(transportation):
                print(str(index+1)+'.',f'{destination} \t') 
            choose = int(input("Select by Number: "))
            if choose not in [i for i in range(1,len(transportation)+1)]:
                raise "ERROR INPUT PLEASE RELOG"
            result.append(transportation[choose-1])
        print('='*35)
    return result

def payment_top_up():
    price = [5000, 10000, 20000, 30000,50000]
    validation = True
    total = 0
    while validation:
        print('='*35)
        print('Welcome to Amazing Bus')
        print(f'Choose your price top up: ')
        for index,pay in enumerate(price):
            print(str(index+1)+'.',f'{pay} \t')
        choose = int(input("Select by Number: "))
        if choose not in [i for i in range(1,len(price)+1)]:
            raise "ERROR INPUT PLEASE RELOG"
        total+=price[choose-1]
        print('='*35)
        choose = str(input("Topup Again? [y/n] "))
        if choose[0].lower() != "y":
            break
    return total

def main():
    emoney = EMoneyCard("Joel")
    while True:
        print("="*35)
        print('Welcome to Amazing Bus')
        print("Choose the menu by number")
        print("1. Top up")
        print("2. Go to Destination")
        print("3. Check Balance")
        print("0. Logout")
        choose = int(input("Select by number: "))
        print("="*35)
        if choose == 1:
            print(emoney.top_up(payment_top_up()))
        elif choose == 2:
            dest = destination()
            halte = Halte(dest[0], dest[1], dest[2])
            halte.totalCost()
            totalCost = halte.getCost()
            return emoney.deduct(totalCost)
        elif choose == 3:
            return f"Your Saldo: {emoney.check_balance()}"
        elif choose == 0:
            return "Thank You"
        else:
            raise "ERROR INPUT PLEASE RELOG"
        
if __name__ == '__main__':
    print(main())