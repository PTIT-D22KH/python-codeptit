# pykt073.py

def main():
    # Write your code here
    n = int(input())
    res = []
    is68 = False
    is7 = False
    len7 = 0
    for _ in range(n):
        a = input().strip().split()
        if (len(res) == 0):
            if (len(a) == 6):
                is68 = True
                res.append(1)
            elif (len(a) == 7):
                is7 = True
                len7 += 1
                res.append(2)
        else:
            if (len(a) == 7 and (is7 == False or len7 == 4)):
                res.append(2)
                is7 = True
                len7 = 1
                is68 = False
            elif (len(a) == 6 and is68 == False):
                res.append(1)
                is68 = True
                is7 = False
            elif (len(a) == 7):
                len7 += 1
    print(len(res))
    for x in res:
        print(x)


        

if __name__ == '__main__':
    main()
