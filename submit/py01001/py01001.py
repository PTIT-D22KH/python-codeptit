# py01001.py
def main():
    # Write your code here
    ok = True
    try:
        s = input()
        n = int(float(s))
        
    except:
        # print("Nhap sai")
        # ok = False
        '''
        Choose number only in input string
        '''
        res = ""
        for x in s:
            if (x.isdigit()):
                res += x
            elif (x == ','):
                res += '.'

        '''
        if the input string do not contain number
        '''
        if (len(res) == 0):
            print("Chuoi ban nhap khong co so!")
            ok = False
        # print(res)
        # ok = False
        if ok == True:
            n = res
            n = int(float(res))
        

    finally:
        if ok == True:
            if (n % 2 == 0) :
                print("CHAN")
            else:
                print("LE")

if __name__ == '__main__':
    main()
