# py02013.py

def main():
    # Write your code here
    while (True):
        n = int(input())
        if n == 0:
            return
        count = 1
        while (n != 1):
            if n % 2 == 0:
                n /= 2
            else:
                n = n * 3 + 1
            count += 1
        print(count)
    

if __name__ == '__main__':
    main()
