import math

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def calDist(self, a):
        return math.sqrt((a.x - self.x) ** 2 + (a.y - self.y) ** 2)

def main():
    n = int(input())
    for i in range(n):
        a, b, c, d = [int(i) for i in input().split()]
        x = Point(a, b)  
        y = Point(c, d)  
        print(f"{x.calDist(y):.4f}") 

if __name__ == '__main__':
    main()