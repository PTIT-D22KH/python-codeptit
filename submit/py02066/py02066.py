# py02066.py

def main():
    # Write your code here
    n = int(input())
    a = []
    while True:
        try:
            x = [int(i) for i in input().split()]
            a.extend(x)

        except:
            break
    max_value = max(a)
    ok = True
    for i in range(1, max_value):
        if i not in a:
            print(i)
            ok = False
    if ok:
        print("Excellent!")

    

if __name__ == '__main__':
    main()
