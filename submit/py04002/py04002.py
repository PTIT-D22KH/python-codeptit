# py04002.py
class Rectangle:
    def __init__(self, height, width, color) -> None:
        self.height = height
        self.width = width
        self.c = color
    def perimeter(self):
        return (self.height + self.width) * 2
    def area(self):
        return self.height * self.width
    def color(self):
        res = self.c[0].upper() + self.c[1:].lower()
        return res

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))