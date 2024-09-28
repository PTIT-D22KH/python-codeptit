# py01025.py

def main():
    # Write your code here
    s = input()
    x = ""
    count = 0
    res = ""
    try:
        # temp = float(s)
        if (s.count(".") > 1):
            raise Exception("So ban nhap vao khong phai so thuc")
        if (s.count(".") == 1):
            if s[0] == '.':
                s = "0" + s
            t = len(s) - 1
            tempDecimalPart = ""
            while (s[t] != '.'):
                if not s[t].isalpha():
                    tempDecimalPart += s[t]
                t -= 1
            tempDecimalPart += s[t]
            tempDecimalPart = tempDecimalPart[::-1]
            # print(tempDecimalPart)
            
            for i in range(t - 1, 0, -1):
                # print(s[i], end = '')
                if (s[i].isdigit()):
                    count += 1
                    x += s[i]
                    if (count == 3):
                        x += ","
                        count = 0
            x += s[0]
            # print(s[t:])
            # x = x + s[t:]
            res = x[::-1]
            res += tempDecimalPart
        else:
            for i in range(len(s) - 1, 0, -1):
                # print(s[i], end = '')
                if (s[i].isdigit()):
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
