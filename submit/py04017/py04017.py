# py04017.py
class Racer:
    def __init__(self, name, crew, endTime):
        self.name = name
        self.crew = crew
        self.id = self.setId()
        self.endTime = endTime
        self.minsTime = self.calMinsTime()
        self.velocity = round(120 / self.minsTime)

    def __str__(self):
        return self.id + " " + self.name + " " + self.crew + " " + str(self.velocity) + " Km/h"

    def setId(self):
        a = self.name.strip().split()
        b = self.crew.strip().split()
        res = ''
        for x in b:
            res += x[0]
        for x in a:
            res += x[0]
        return res
    
    def calMinsTime(self):
        a = self.endTime.strip().split(":")
        hours = int(a[0]) - 6
        minutes = int(a[1])
        return (hours * 60 + minutes) / 60
def cmp(a):
    return (a.minsTime)
def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        a.append(Racer(input(), input(), input()))
    a.sort(key = cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()
