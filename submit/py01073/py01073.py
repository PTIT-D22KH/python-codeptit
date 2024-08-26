# py01073.py


def main():
    # Write your code here
    global s, n, used
    s = input()
    n = len(s)
    used = [0] * n
    
    Try("", 0)



def Try(res, i):
    if (i == n):
        print(res)
    for j in range(n):
        if(used[j] == 0):
            used[j] = 1
            Try(res + s[j], i + 1)
            used[j] = 0
if __name__ == '__main__':
    main()
