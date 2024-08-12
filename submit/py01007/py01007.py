# py01007.py
import math
def main():
    # Write your code here
    for t in range(int(input())):
        n, x, m = [float(i) for i in input().split()]
        # m = n * (1 + x) ^ res
        res = math.log(m / n, (1 + x / 100))
        print(math.ceil(res))


if __name__ == '__main__':
    main()
