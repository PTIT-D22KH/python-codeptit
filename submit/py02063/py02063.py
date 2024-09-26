# py02063.py

def main():
    # Write your code here
    n = int(input())
    a  = [int(i) for i in input().split()]
    a.sort()

    max_product1 = a[-1] * a[-2]
    max_product2 = a[-1] * a[-2] * a[-3]
    max_product3 = a[0] * a[1] * a[-1]
    print(max(max_product1, max_product2, max_product3))
    

if __name__ == '__main__':
    main()
