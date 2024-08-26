# py01036.py

def main():
    # Write your code here
    for t in range(int(input())):
        n = int(input())
        res = 0.0
        if (n % 2 == 1):
            for i in range(1, n + 1, 2):
                # print(res)
                # print(float(1.0/n))
                res += 1.0 / i
        else:
            for i in range(2, n + 1, 2):
                # print(res)
                # print(float(1.0/n))
                res += 1.0 / i
        print(f"{res:.6f}")
        

if __name__ == '__main__':
    main()
