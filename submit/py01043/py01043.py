# py01043.py
def isPalindrome(n):
    reversed_n = n[::-1]
    if (len(n) % 2 == 1):
        return False
    if (n != reversed_n):
        return False
    for c in n:
        if (int(c) % 2 == 1):
            return False
    return True

def testCase() :
    n = input()
    for i in range(10, int(n)):
        if(isPalindrome(str(i))):
            print(i, end = ' ')

    
def main():
    # Write your code here
    for t in range(int(input())):
        testCase()
        print()

if __name__ == '__main__':
    main()
