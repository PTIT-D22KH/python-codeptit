# icpc0106.py

def main():
    # Write your code here
    for _ in range(int(input())):
        b = int(input())
        s = input()
        s = int(s, 2)
        res = ""
        digit = "ABCDEF"
        r = s
        while r > 0:
            if b > 10:
                m = r % b
                if m >= 10:
                    res += digit[m - 10]
                else:
                    res += str(m)
            else:
                res += str(r % b)
            r //= b
        print(res[::-1])



if __name__ == '__main__':
    main()
