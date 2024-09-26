# py02010.py

def main():
    # Write your code here
    while True:
        x = input()
        if x == '0':
            break
        t = int(x)
        a = []
        for _ in range(t):
            a.append(int(input()))
        min_val = min(a)
        max_val = max(a)
        if min_val == max_val:
            print("BANG NHAU")
        else:
            print(f"{min_val} {max_val}")


if __name__ == '__main__':
    main()
