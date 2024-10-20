# py04018.py
class Contestant:
    count = 0
    def __init__(self, name, contestId, itScore, majorScore):
        Contestant.count += 1
        self.id = f"GV{Contestant.count:02d}"
        self.name = name
        self.contestId = contestId
        self.itScore = float(itScore)
        self.majorScore = float(majorScore)
        self.priorityId = contestId[1]
        self.major = self.calMajor(contestId[0])
        self.priorityScore = self.calPriorityScore()
        self.result = self.calResult()
    
    def calMajor(self, s):
        if s == 'A':
            return 'TOAN'
        elif s == 'B':
            return 'LY'
        return 'HOA'
    def calPriorityScore(self):
        if self.priorityId == '1':
            return 2.0
        elif self.priorityId == '2':
            return 1.5
        elif self.priorityId == '3':
            return 1.0
        return 0.0
    
    def calResult(self):
        score = self.itScore * 2 + self.majorScore + self.priorityScore
        self.totalScore = score
        if score >=18:
            return "TRUNG TUYEN"
        return "LOAI"
    def __str__(self):
        return self.id + " " + self.name + " " + self.major + f" {self.totalScore:.1f} " + self.result

def cmp(a) :
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
