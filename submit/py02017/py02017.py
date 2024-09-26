# py02017.py

def main():
    # Write your code here
    for t in range(int(input())):
        res = {}
        n = int(input())
        a = [int(i) for i in input().split()]
        for x in a:
            if (x not in res.keys()):
                res[x] = 1
            else:
                res[x] += 1
        for x, fre in res.items():
            if (fre % 2 == 1):
                print(x)
                break
        

if __name__ == '__main__':
    main()
