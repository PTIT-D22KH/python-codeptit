# icpc0116.py

def main():
    # Write your code here
    for t in range(int(input())):
        x = input()
        if x[0] == x[-1]:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
