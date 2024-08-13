# py01011.py
def check(n):
    # n = input()
    l = len(n)
    x = n[-1::-1]
    # print(x)
    a = int(n)
    b = int(x)
    if (a != b):
        return False
    if (l % 2 != 0):
        return False
    for c in n:
        if (c not in ['0', '2', '4', '6', '8']):
            return False
    return True
def main():
    # Write your code here
    for t in range(int(input())):
        n = input()
        count = 0
        for i in range(0, int(n)):
            if (check(str(i)) == True):
                print(i, end = " ")

        print()
if __name__ == '__main__':
    main()
