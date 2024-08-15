# py01051.py

def main():
    # Write your code here
    for t in range(int(input())):
        n = input()
        sumDigits = 0
        for c in n:
            sumDigits += int(c)
        rev = str(sumDigits)[::-1]
        if (len(rev) > 1  and rev == str(sumDigits)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
