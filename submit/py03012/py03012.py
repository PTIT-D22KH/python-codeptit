class Student:
    def __init__(self, name, numAC, totalSubmit) -> None:
        self.name = name
        self.numAC = numAC
        self.totalSubmit = totalSubmit

    def __str__(self):
        return f"{self.name} {self.numAC} {self.totalSubmit}"

def cmp(a):
    return (-a.numAC, a.totalSubmit, a.name)

def main():
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        numAC, totalSubmit = [int(i) for i in input().split()]
        a.append(Student(name, numAC, totalSubmit))
    a.sort(key=cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()