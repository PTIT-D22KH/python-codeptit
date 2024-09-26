# icpc0108.py

def main():
    # Write your code here
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        a.sort()
        count = 0
        for i in range(0, len(a) - 2):
            l = i + 1
            r = len(a) - 1
            x = a[i]
            while l < r:
                temp = x + a[l] + a[r]
                if temp == 0:
                    count += 1
                    l += 1
                elif temp < 0:
                    l += 1
                else:
                    r -= 1
        print(count)

if __name__ == '__main__':
    main()
