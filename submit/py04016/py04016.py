# py04016.py
import datetime

class Customer:
    count = 0

    def __init__(self, name, room, startDate, endDate, additionalCost):
        Customer.count += 1
        self.id = f"KH{Customer.count:02d}"
        self.name = name.strip()
        self.room = room.strip()
        self.startDate = datetime.datetime.strptime(startDate.strip(), "%d/%m/%Y")
        self.endDate = datetime.datetime.strptime(endDate.strip(), "%d/%m/%Y")
        self.additionalCost = int(additionalCost)
        self.numDays = (self.endDate - self.startDate).days + 1
        self.calTotalCost()
    
    def calTotalCost(self):
        c = self.room[0]
        totalCost = 0
        if c == '1':
            self.totalCost =  self.numDays * 25 + self.additionalCost
        elif c == '2':
            self.totalCost =  self.numDays * 34 + self.additionalCost
        elif c == '3':
            self.totalCost =  self.numDays * 50 + self.additionalCost
        else:
            self.totalCost =  self.numDays * 80 + self.additionalCost




    def __str__(self):
        start_date_str = self.startDate.strftime("%d/%m/%Y")
        end_date_str = self.endDate.strftime("%d/%m/%Y")
        return f"{self.id} {self.name} {self.room} {self.numDays} {self.totalCost}"

def cmp(a):
    return (-a.totalCost)
def main():
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        room = input()
        startDate = input()
        endDate = input()
        additionalCost = input()
        a.append(Customer(name, room, startDate, endDate, additionalCost))
    a.sort(key = cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()