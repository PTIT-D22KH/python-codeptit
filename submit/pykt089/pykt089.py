# pykt089.py

def main():
    # Write your code here
    n = int(input())
    a = []
    while True:
        try:
            a.extend([int(i) for i in input().split()])
        except:
            break
    even = [i for i in a if i % 2 == 0]
    odd = [i for i in a if i % 2 == 1]
    even.sort()
    odd.sort(key = lambda x : -x)
    currEven = 0
    currOdd =0 
    for x in a:
        if x % 2 == 0:
            print(even[currEven], end = ' ')
            currEven += 1
        else:
            print(odd[currOdd], end = ' ')
            currOdd += 1
    


if __name__ == '__main__':
    main()
