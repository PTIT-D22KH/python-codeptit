# py01047.py
import math
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def main():
    # Write your code here
    for t in range(int(input())):
        s = input()[-4:]
        if (isPrime(int(s))):
            print("YES")
        else :
            print("NO")

if __name__ == '__main__':
    main()
