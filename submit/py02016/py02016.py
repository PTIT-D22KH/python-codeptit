# py02016.py

def main():
    # Write your code here
    for t in range(int(input())):
        n = int(input())
        fre = dict()
        a = [int(i) for i in input().split()]
        b = []
        for x in a:
            if x not in fre:
                fre[x] = 1
            else:
                fre[x] += 1
        maxFre = max(fre.values())
        minNum = int(1e7)
        for f, s in fre.items():
            if s == maxFre:
                maxFre = s
                minNum = min(minNum, f)
        if (maxFre > n // 2):
            print(minNum)
        else:
            print("NO")



if __name__ == '__main__':
    main()
