# pykt090.py

def main():
    # Write your code here
    
    # with open("pykt090/CONTACT.in", "r") as file:
    with open("CONTACT.in", "r") as file:
        d = {}
        while True:
            s = file.readline().strip().lower()
            # print(s)
            if not s:
                break
            if s not in d:
                d[s]  = 1
            else:
                d[s] += 1
        a = []
        for k in d.keys():
            a.append(k)
        a.sort()
        for x in a:
            print(x)


if __name__ == '__main__':

    main()
