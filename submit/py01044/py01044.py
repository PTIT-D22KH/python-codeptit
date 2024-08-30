# py01044.py

def main():
    # Write your code here
    a = input().strip().lower().split()
    b = input().strip().lower().split()
    # print(a)
    # print(b)
    c = a.copy()
    c.extend(b)
    union = list(set(c))
    union.sort()
    intersection = []
    for x in a:
        if x in b:
            intersection.append(x)
    intersection.sort()
    for x in union:
        print(x, end = ' ')
    print()
    for x in intersection:
        print(x, end = ' ')

if __name__ == '__main__':
    main()
