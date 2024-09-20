# py02025.py

def main():
    # Write your code here
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    intersection = []
    sub_a = []
    sub_b = []
    for x in b:
        if x in a:
            intersection.append(x)
        else:
            sub_b.append(x)
    for x in a:
        if x not in b:
            sub_a.append(x)
    for x in intersection:
        print(x, end = ' ')
    print()
    for x in sub_a:
        print(x, end = ' ')
    print()
    for x in sub_b:
        print(x, end = ' ')
    print()


if __name__ == '__main__':
    main()
