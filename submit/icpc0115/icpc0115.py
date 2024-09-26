# icpc0115.py
def factorial(n):
    res = 1
    for i in range(2, n + 1) :
        res *= i
    return res
def check(x):
    res = 0
    for c in x:
        res += factorial(int(c))
    # print(res)
    if (res == int(x)):
        return True
    else:
        return False
def main():
    # Write your code here
    for t in range(int(input())):
        x = input()
        if (check(x)):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
