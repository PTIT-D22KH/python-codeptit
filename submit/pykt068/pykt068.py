# pykt068.py
class Subject:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
    def __str__(self):
        return self.id + " " + self.name + " "  + self.type

def cmp(a):
    return a.id
def main():
    # Write your code here
    a = []
    for _ in range(int(input())):
        a.append(Subject(input(), input(), input()))
    a.sort(key=cmp)
    for x in a:
        print(str(x))


if __name__ == '__main__':
    main()
