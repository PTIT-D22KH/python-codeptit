# py04009.py
class ComplexNumber():
    def __init__(self, real, image) -> None:
        self.real = real
        self.image = image
    
    def addComplexNumber(self, other) :
        r = self.real + other.real
        i = self.image + other.image
        return ComplexNumber(r, i)
    
    def multiplyComplexNumber(self, other):
        r = self.real * other.real - self.image * other.image
        i = self.image * other.real + self.real * other.image
        return ComplexNumber(r, i)
    
    def __str__(self) -> str:
        res = str(self.real)
        if (self.image > 0) :
            res += " + " + str(self.image) + "i"
        else:
            res += " - " + str(self.image * -1) + "i"
        return res

def main():
    # Write your code here
    for t in range(int(input())):
        a, b, c, d = [int(i) for i in input().split()]
        x = ComplexNumber(a, b)
        y = ComplexNumber(c, d)
        res1 = x.addComplexNumber(y).multiplyComplexNumber(x)
        res2 = (x.addComplexNumber(y)).multiplyComplexNumber(x.addComplexNumber(y))
        print(str(res1) + ", " + str(res2))

if __name__ == '__main__':
    main()
