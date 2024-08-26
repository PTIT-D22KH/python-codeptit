# py02020.py
def main():
    # Write your code here
    n = int(input())
    a = [float(i) for i in input().split()]
    minn = min(a)
    maxx = max(a)
    for x in a:
        if x == minn or x == maxx:
            a.remove(x)
    sum = 0.0
    for x in a:
        sum += x
    print(round(sum / len(a), 2))
if __name__ == '__main__':
    main()
