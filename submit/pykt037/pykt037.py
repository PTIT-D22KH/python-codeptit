# pykt037.py

def main():
    # Write your code here
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for t in range(int(input())):
        n, b = [int(i) for i in input().split()]
        res = ""
        if n == 0:
            print("0")
        else:

            while n > 0:
                r = n % b
                res = digits[r] + res
                n //= b
            print(res)


if __name__ == '__main__':
    main()
