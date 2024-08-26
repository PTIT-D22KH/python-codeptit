# icpc0104.py
def isdigit(c):
    if (c >= '0' and c <= '9'):
        return True
    return False
def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        res = 0
        curr = 0
        for c in s:
            
            if (isdigit(c)):
                # print(c)
                curr = curr * 10 + int(c)
                # print(res)
                # print(curr)
            else:
                if curr != 0:
                    res = max(res, curr)
                curr = 0
        if curr != 0:
            res = max(res, curr)
        # res = min(res, curr)
        print(res)

if __name__ == '__main__':
    main()
