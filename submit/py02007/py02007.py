# py02007.py

def main():
    # Write your code here
    a = [int(i) % 42 for i in input().split()]
    res = set(a)
    print(len(res))

if __name__ == '__main__':
    main()
