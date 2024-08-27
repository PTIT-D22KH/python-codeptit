# icpc0107.py
def minChange(x):
    res = ""
    for c in x:

        if int(c) == int(q):
            res += str(p)
        else:
            res += c
    return int(res)
def maxChange(x):
    res = ""
    for c in x:

        if int(c) == int(p):
            res += str(q)
        else:
            res += c
    return int(res)
def main():
    # Write your code here
    for t in range(int(input())):
        global p , q 
        p, q =  [int(i) for i in input().split()]
        x = min(p, q)
        y = max(p, q)
        p = x
        q = y
        x1 = input()
        x2 = input()
        minRes = minChange(x1) + minChange(x2)
        maxRes = maxChange(x1) + maxChange(x2)
        print(minRes, maxRes)

if __name__ == '__main__':
    main()
