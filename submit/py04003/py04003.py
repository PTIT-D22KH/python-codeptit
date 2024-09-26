# py04003.py
import math
class Fraction:
    def __init__(self, numerator, denominator) -> None:
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    def simplify(self):
        a = math.gcd(self.denominator, self.numerator)
        self.denominator /= a
        self.numerator /= a
    def __str__(self) -> str:
        res = f"{self.numerator:.0f}/{self.denominator:.0f}"
        return res
    
def main():
    # Write your code here
    a, b = [int(i) for i in input().split()]
    x = Fraction(a, b)
    print(str(x))

if __name__ == '__main__':
    main()
