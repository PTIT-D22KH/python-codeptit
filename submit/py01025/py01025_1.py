# py01025.py

def main():
    # Write your code here
    s = input()
    x = ""
    count = 0
    res = ""
    try:
        temp = float(s)
        if (s.count(".") > 1):
            raise Exception("So ban nhap vao khong phai so thuc")
        if (s.count(".") == 1):
            t = len(s) - 1
            while (s[t] != '.'):
                t -= 1
            
            for i in range(t - 1, 0, -1):
                # print(s[i], end = '')
                
                count += 1
                x += s[i]
                if (count == 3):
                    x += ","
                    count = 0
            x += s[0]
            # print(s[t:])
            # x = x + s[t:]
            res = x[::-1]
            res += s[t:]
        else:
            for i in range(len(s) - 1, 0, -1):
                # print(s[i], end = '')
                count += 1
                x += s[i]
                if (count == 3):
                    x += ","
                    count = 0
            x += s[0]
            res = x[::-1]
        print(res)
    except :
        raise Exception("So ban nhap vao khong phai so thuc")
    

        

if __name__ == '__main__':
    main()
