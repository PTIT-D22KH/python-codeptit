# py01016.py

def main():
    # Write your code here
    for t in range(int(input())):
        s = input()
        res = ""
        for i in range(1, len(s), 2):
            x = int(s[i])
            for j in range(0, x):
                res = res + s[i - 1]
        print(res)

if __name__ == '__main__':
    main()
