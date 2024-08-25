# py02018.py

def main():
    # Write your code here
    n = int(input())
    a = [int(i) for i in input().split()]
    minn = min(a)
    maxx = max(a)
    for i in range(minn, maxx+ 1):
        if i not in a:
            print(i)
            return
    print(maxx+1)        

if __name__ == '__main__':
    main()
