# pykt038.py

def main():
    # Write your code here
    base = 3
    x = input()
    while (len(x) % 3 != 0):
        x = "0" + x
    group = [x[i:i + 3] for i in range(0, len(x), 3)]

    res = [str(int(i, 2)) for i in group]

    print(''.join(res))
    

        
    

if __name__ == '__main__':
    main()
