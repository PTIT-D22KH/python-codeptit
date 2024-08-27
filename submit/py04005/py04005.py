# py04005.py
import math
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, a):
        res =  math.sqrt((a.x - self.x) ** 2 + (a.y - self.y) ** 2)
        return f"{res:.4f}"
class Edge:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.length = float(self.a.distance(self.b))
class Triangle:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
    def isValid(self):
        if (self.a.length <= 0 or self.b.length <= 0 or self.c.length <= 0 or self.a.length + self.b.length <= self.c.length or self.a.length + self.c.length <= self.b.length or self.b.length + self.c.length <= self.a.length):
            return False
        return True
    def calPerimeter(self):
        return self.a.length + self.b.length + self.c.length
def main():
    # Write your code here
    for t in range(int(input())):
        a, b, c, d, e,f = [int(i) for i in input().split()]
        x = Point(a, b)
        y = Point(c, d)
        z = Point(e, f)
        edge1 = Edge(x, y)
        edge2 = Edge(y, z)
        edge3 = Edge(x, z)
        res = Triangle(edge1, edge2, edge3)
        if res.isValid() == False:
            print("INVALID")
        else:
            print(f"{res.calPerimeter():.3f}")


if __name__ == '__main__':
    main()
