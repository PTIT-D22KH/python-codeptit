# py01010.py

def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        a = s[0:2]
        b = s[-2:]
        # print(a, b)
        if (a == b) :
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
