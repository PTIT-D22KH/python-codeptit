# pykt074.py

def main():
    # Write your code here
    n = int(input())
    for _ in range(n):
        s = input()
        a = s.strip().split(" ")
        m = len(a)
        res = ""
        for i in range(m):
            if (len(res) + len(a[i]) + 1 <= 100):
                res += a[i] + " "
        # print(len(res))
        print(res)
    

if __name__ == '__main__':
    main()
