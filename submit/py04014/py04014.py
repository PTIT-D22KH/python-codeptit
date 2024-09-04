# py04014.py
class Student:
    count = 0
    def __init__(self, name, score_list) -> None:
        self.name = name
        Student.count += 1
        self.id = f"HS{Student.count:02d}"
        self.score_list = score_list
        totalScore = score_list[0] * 2 + score_list[1] * 2
        for i in range(2, len(score_list)):
            totalScore += score_list[i]
        self.avgScore = totalScore / 12.0
        result = ""
        if (self.avgScore >= 9):
            result = "XUAT SAC"
        elif self.avgScore >= 8:
            result = "GIOI"
        elif self.avgScore >= 7:
            result = "KHA"
        elif self.avgScore >= 5:
            result = "TB"
        else:
            result = "YEU"
        self.result = result
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.avgScore:.1f} {self.result}"

def main():
    # Write your code here
    n = int(input())
    a = []
    for _ in range(n):
        name = input()
        score_list = [float(i) for i in input().split()]
        a.append(Student(name, score_list))
    a.sort(key = lambda x : (-x.avgScore, x.id))
    for x in a:
        print(str(x))


if __name__ == '__main__':
    main()
