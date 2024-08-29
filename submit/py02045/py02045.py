# py02045.py

def main():
    # Write your code here
    x = input()
    while (len(x) > 1):
        n = len(x)
        mid = n // 2
        first_half = int(x[:mid].strip())
        second_half =int(x[mid:].strip())
        # print(first_half, second_half)
        x = str(first_half + second_half)
        print(x)
    

if __name__ == '__main__':
    main()
