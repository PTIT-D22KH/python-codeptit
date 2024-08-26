# py01042.py
def testCase():
    s = input()
    for char in s:
        if (char != '0' and char != '1' and char != '2'):
            print("NO")
            return
    print("YES")
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()
        

if __name__ == '__main__':
    main()
