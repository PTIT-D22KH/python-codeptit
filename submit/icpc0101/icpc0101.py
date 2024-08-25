# icpc0101.py

def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    res = []
    for x in a:
        if len(res) == 0:
            res.append(x)
        else:
            if ((res[-1] + x) % 2 == 0):
                a.pop()
            else:
                res.append(x)
    print(len(res))

if __name__ == '__main__':
    main()
