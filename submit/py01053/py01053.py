# py01053.py

def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        sumDigits = 0
        for c in s:
            sumDigits += int(c)
        if (sumDigits % 3 == 0):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
