# py01020.py

def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        if (s[-2:] == '86'):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
