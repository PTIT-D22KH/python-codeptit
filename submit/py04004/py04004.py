# py04004.py
import math
def lcm(a, b):
    return a * b / math.gcd(a,b)
class Fraction:
    def __init__(self, numerator, denominator) -> None:
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        self.simplify()
    def simplify(self):
        a = math.gcd(self.denominator, self.numerator)
        self.denominator //= a
        self.numerator //= a
    def __str__(self) -> str:
        res = f"{self.numerator:.0f}/{self.denominator:.0f}"
        return res
    def sumFraction(self, other):
        r = lcm(self.denominator, other.denominator)
        x = r / self.denominator * self.numerator + r / other.denominator * other.numerator
        res = Fraction(x, r)
        res.simplify()
        return res
def main():
    # Write your code here
    a, b, c, d= [int(i) for i in input().split()]
    x = Fraction(a, b)
    y = Fraction(c, d)
    print(str(x.sumFraction(y)))

if __name__ == '__main__':
    main()
