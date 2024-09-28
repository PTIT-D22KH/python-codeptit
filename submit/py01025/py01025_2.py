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

            integerPart = ""
            for i in range(t - 1, 0, -1):
                # print(s[i], end = '')
                if (s[i].isdigit()):
                    integerPart += s[i]
            integerPart += s[0]

            # print(tempDecimalPart)
            # integerPart = s[:t]
            # print(integerPart)
            integerPart = str(int(integerPart))
            x = ""
            for i in range(0, len(integerPart) - 1, 1):
                if (integerPart[i].isdigit()):
                    count += 1
                    x += integerPart[i]
                    # print(x)
                    if (count == 3):
                        x += ","
                        count = 0
            x += integerPart[-1]

            


            # for i in range(t - 1, 0, -1):
            #     # print(s[i], end = '')
            #     if (s[i].isdigit()):
            #         count += 1
            #         x += s[i]
            #         if (count == 3):
            #             x += ","
            #             count = 0
            # x += s[0]
            
            # print(s[t:])
            # x = x + s[t:]
            # print(x)
            # res = x[::-1]
            # res = str(int(res))
            res = x[::-1]
            
            curr = 0
            while (res[curr] == '0' or not res[curr].isdigit()):
                curr += 1
            res = res[curr:]
            res += tempDecimalPart
            
        else:
            s = str(int(s))
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
            curr = 0
            while (res[curr] == '0' or not res[curr].isdigit()):
                curr += 1
            res = res[curr:]
        print(res)
    except :
        raise Exception("So ban nhap vao khong phai so thuc")
    

        

if __name__ == '__main__':
    main()
