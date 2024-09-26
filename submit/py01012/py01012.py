# py01012.py

def main():
    # Write your code here
    s1 = input()
    s2 = input()
    p = int(input())
    p -= 1
    result = s1[:p] + s2 + s1[p:]
    print(result)

if __name__ == '__main__':
    main()
