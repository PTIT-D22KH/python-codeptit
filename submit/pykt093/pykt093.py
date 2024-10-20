# pykt093.py
import math
class Student:
    count = 0
    def __init__(self, name, score1, score2, score3):
        Student.count += 1
        self.id = f"SV{Student.count:02d}"
        self.name = self.formatName(name)
        self.score1 = float(score1)
        self.score2 = float(score2)
        self.score3 = float(score3)
        self.totalScore = math.ceil((self.score1 * 3 + self.score2 * 3 + self.score3 * 2) / 8.0 * 100) / 100
        self.rank = 0
    def formatName(self, name):
        a = name.strip().lower().split(" ")
        res = ""
        for x in a:
            res += x.strip().title() + " "
        return res
    def __str__(self):
        return self.id + " " + self.name + f"{self.totalScore:.2f} {self.rank}"

def cmp(a):
    return (-a.totalScore)
def main():
    # Write your code here
    n = int(input())
    a = []
    for i in range(n):
        a.append(Student(input(), input(), input(), input()))
    rank = 0
    a.sort(key = cmp)
    for i in range(n):
        if i == 0 or a[i].totalScore != a[i - 1].totalScore:
            rank = i + 1
        a[i].rank = rank
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()
