# pykt092.py
class Contestant:
    count = 0
    def __init__(self, name, score, ethnic, area):
        Contestant.count += 1
        self.id = f"TS{Contestant.count:02d}"
        self.name = self.formatName(name)
        self.score = float(score)
        self.ethnic = ethnic
        self.area = area
        self.priorityScore = self.calPriorityScore()
        self.totalScore = self.score + self.priorityScore
        if self.totalScore >= 20.5:
            self.result = "Do"
        else:
            self.result = 'Truot'
    def formatName(self, name):
        a = name.strip().lower().split(" ")
        res = ""
        for x in a:
            res += x.strip().title() + " "
        return res
    def calPriorityScore(self):
        res = 0
        if self.ethnic != 'Kinh':
            res += 1.5
        if self.area == '1':
            res += 1.5
        elif self.area == '2':
            res += 1
        return res
    def __str__(self):
        return self.id + " " + self.name + f" {self.totalScore:.1f} {self.result}"
        

def cmp(a)  :
    return (-a.totalScore)
def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        a.append(Contestant(input(), input(), input(), input()))
    a.sort(key = cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()
