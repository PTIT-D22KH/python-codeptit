# py04010.py
class Contestant:
    def __init__(self, name, dob, score1, score2, score3) -> None:
        self.name = name
        self.dob = dob
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.totalScore = (score1 + score2 + score3)
    
    def __str__(self) -> str:
        res = self.name + " " + self.dob + f" {self.totalScore:.1f}"
        return res
def main():
    # Write your code here
    name = input()
    dob = input()
    score1 = float(input())
    score2 = float(input())
    score3 = float(input())
    res = Contestant(name, dob, score1, score2, score3)
    print(res)

if __name__ == '__main__':
    main()
