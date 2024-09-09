# py04015.py
class Customer:
    count = 0
    def __init__(self, name, oldNum, newNum) -> None:
        Customer.count += 1
        self.id = f"KH{Customer.count:02d}"
        self.name = name
        self.numUsed = int(newNum) - int(oldNum)
        self.totalCost = self.calTotalCost()
    def calTotalCost(self):
        basicCost = 0
        # additionalCost = 0
        if (self.numUsed <= 50):
            basicCost = 100 * self.numUsed
            return int(basicCost * 1.02)
        elif (self.numUsed <= 100):
            basicCost = 100 * 50 +  150  * (self.numUsed - 50)
            return int(basicCost * 1.03)
        else:
            basicCost = 50 * 100 + 150 * 50 + 200 * (self.numUsed - 100)
            return int(basicCost * 1.05)

    def __str__(self) -> str:
        return self.id + " " + self.name + " " + str(self.totalCost)
def cmp(a):
    return (-a.totalCost)
def main():
    # Write your code here
    n = int(input())
    a = []
    for _ in range(n):
        a.append(Customer(input(), input(), input()))
    a.sort(key = cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()
