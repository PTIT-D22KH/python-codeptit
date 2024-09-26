# pykt099.py

def main():
    # Write your code here
    a = set()
    b = set()
    # with open("pykt099/DATA1.in", "r") as file:
    with open("DATA1.in", "r") as file:
        while True:
            s = file.readline().strip()
            if not s:
                break
            temp = s.split()
            for x in temp:
                a.add(x.lower())
    # with open("pykt099/DATA2.in", "r") as file:
    with open("DATA2.in", "r") as file:
        while True:
            s = file.readline().strip()
            if not s:
                break
            temp = s.split()
            for x in temp:
                b.add(x.lower())  
    res1 = [] 
    res2 = []
    for x in a:
        if x not in b:
            res1.append(x)
    
    for x in b:
        if x not in a:
            res2.append(x)
    res1.sort()
    res2.sort()
    for x in res1:
        print(x, end = ' ')
    print()
    for x in res2:
        print(x, end = ' ')


if __name__ == '__main__':
    main()
