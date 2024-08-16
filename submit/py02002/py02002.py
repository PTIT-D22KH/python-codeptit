# py02002.py

def main():
    # Write your code here
    fibo = [0] * 93
    fibo[1] = 1
    for i in range(2, 93):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    for t in range(int(input())):
        a, b = [int(i) for i in input().split()]
        for i in range(a, b + 1):
            print(fibo[i], end = ' ')
        print()

if __name__ == '__main__':
    main()
