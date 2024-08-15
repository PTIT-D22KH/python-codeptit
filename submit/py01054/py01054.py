# py01054.py

def main():
    # Write your code here
    for t in range(int(input())):
        n = input()
        res = 1
        for c in n:
            if (c != '0'):
                res *= int(c)
        print(res)

if __name__ == '__main__':
    main()
