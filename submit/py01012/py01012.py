# py01012.py

def main():
    # Write your code here
    s1 = input()
    s2 = input()
    p = int(input())
    for i in range(len(s1)):
        if (i + 1 == p):
            print(s2, end = '')
        else:
            print(s1[i], end = '')

if __name__ == '__main__':
    main()
