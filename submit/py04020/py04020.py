# py04020.py
class Bill:
    def __init__(self, id, name, numBuy, singlePrice, discount):
        self.id = id
        self.name = name
        self.numBuy = int(numBuy)
        self.singlePrice = int(singlePrice)
        self.discount = int(discount)
        self.totalPrice = self.numBuy * self.singlePrice - self.discount
    
    def __str__(self):
        return self.id + " " + self.name + " " + str(self.numBuy) + " " + str(self.singlePrice) + " " + str(self.discount) + " " + str(self.totalPrice)
        
def cmp(a):
    return (-a.totalPrice)
def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        a.append(Bill(input(), input(), input(), input(), input()))
    a.sort(key = cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()
