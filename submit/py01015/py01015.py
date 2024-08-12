# py01015.py
def check(s):
    for i in range(0, len(s) - 1):
        if (s[i + 1] < s[i]):
            return False
    return True
def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        if (check(s)):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
