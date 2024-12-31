# pykt098.py
def check(s) :
    if (len(s) >= 10):
        return True
    try:
        n = int(s)
        return False
    except:
        return True
    
def main():
    # Write your code here
    a = []
    with open("DATA.in", 'r') as file:
        x = file.readlines()
        for y in x:
            s = y.split()
            for t in s:
                if (check(t)):
                    a.append(t)
    a.sort()
    for x in a:
        print(x, end = ' ')
    


if __name__ == '__main__':
    main()
