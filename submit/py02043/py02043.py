# py02043.py

def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        x = input()
        a = s.split(x)
        print(len(a) - 1)

if __name__ == '__main__':
    main()
