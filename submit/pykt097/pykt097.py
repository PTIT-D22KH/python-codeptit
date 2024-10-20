# pykt097.py

def main():
    # Write your code here
    delimiter = ".!?"
    a = []
    while True:
        try:
            s = input().strip().lower()
            x = ''
            for i in s:
                if i in delimiter:
                    i = i.strip()
                    if (len(i) > 0):
                        x += i
                        a.append(x)
                    x = ''
                else:
                    x += i
            x = x.strip()
            if (len(x) > 0) :
                a.append(x)

        except:
            break
    # print(a)
    for x in a:
        b = x.strip().split(" ")
        # print(b)
        temp = ''
        for c in b:
            
            if (len(c) > 0):
                
                # print(c)
                if c not in delimiter:
                    temp += c.strip() + " "
                else:
                    temp = temp.strip() + c.strip()
        temp = temp.strip()
        if temp[-1] not in delimiter:
            temp += '.'
        d = temp.strip().split(" ")
        res = ''
        res += d[0].title() + " "
        for i in range(1, len(d)):
            res += d[i] + " "
        print(res.strip())

        # print(x)



if __name__ == '__main__':
    main()
