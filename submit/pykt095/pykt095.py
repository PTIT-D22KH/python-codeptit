# pykt095.py
class Customer:
    count = 0

    def __init__(self, name, info):
        Customer.count += 1
        self.id = f"KH{Customer.count:02d}"
        self.name = self.formatName(name.strip())
        a = info.strip().split()
        self.type = a[0]
        self.numUsed = int(a[2]) - int(a[1])
        self.cost, self.additionalCost, self.vatCost, self.totalCost = self.calCost()

    def formatName(self, name):
        a = name.strip().lower().split()
        res = ""
        for x in a:
            if len(x) == 0:
                continue
            res += x.strip().title() + " "
        return res.strip()

    def calCost(self):
        threshold = 0
        cost = 0
        additionalCost = 0
        vatCost = 0
        totalCost = 0
        if self.type == 'A':
            threshold = 100
        elif self.type == 'B':
            threshold = 500
        else:
            threshold = 200
        if self.numUsed > threshold:
            additionalCost = (self.numUsed - threshold) * 1000
            cost = threshold * 450
            vatCost = additionalCost // 20
        else:
            cost = self.numUsed * 450
        totalCost = cost + additionalCost + vatCost
        return cost, additionalCost, vatCost, totalCost

    def __str__(self):
        return f"{self.id} {self.name} {self.cost} {self.additionalCost} {self.vatCost} {self.totalCost}"

def cmp(a):
    return -a.totalCost

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(Customer(input(), input()))
    a.sort(key=cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()