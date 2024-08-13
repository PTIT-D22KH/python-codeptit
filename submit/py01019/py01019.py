# py01019.py
def testCase():
    s = input()
    reversed_s = s[::-1]
    # print(ord((s[0])))
    for i in range(1, len(s)):
        if(abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(reversed_s[i]) - ord(reversed_s[i - 1]))) :
            print("NO")
            return
    print("YES")
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()
        

if __name__ == '__main__':
    main()
