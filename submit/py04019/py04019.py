# py04019.py
class Contestant:
    count = 0

    def __init__(self, name, ltScore, thScore) -> None:
        Contestant.count += 1
        self.id = f"TS0{Contestant.count}"
        self.name = name
        self.ltScore = normalizeScore(ltScore)
        self.thScore = normalizeScore(thScore)
        self.avgScore = self.calAvgScore()
        self.result = self.calResult()
    
 
    def calAvgScore(self):
        return round((self.ltScore + self.thScore) / 2.0, 2)
    def calResult(self):
        if (self.avgScore > 9.5):
            return "XUAT SAC"
        elif (self.avgScore >= 8):
            return "DAT"
        elif (self.avgScore >= 5):
            return "CAN NHAC"
        return "TRUOT"
    
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + f"{self.avgScore:.2f}" + " " + self.result
def normalizeScore(score):
    score_float = float(score)
    score_int = int(score_float)
    if (score_int > 10):
        score = score[:1] + "." + score[1:]
        return float(score)
    return score_float
def cmp(a: Contestant) :
    return (-a.avgScore)
def main():
    # Write your code here
    n = int(input())
    a = []
    for _ in range(n):
        a.append(Contestant(input(), input(), input()))
    a.sort(key = cmp)
    for x in a:
        print(str(x))
if __name__ == '__main__':
    main()
