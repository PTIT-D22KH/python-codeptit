import math
size = 1000 + 1
era = [1] * size
primes = []
def sieve(size):

    era[0] = 0
    era[1] = 0
    for i in range(2, size):
        if era[i] == 1:
            for j in range(i * i, size, i):
                era[j] = 0
            primes.append(i)

def main():
    s = input()
    input_list = s.split()
    if len(input_list) != 2:
        raise Exception("Input khong hop le! Input phai co so 2 so nguyen n va m")
    try:
        n, m = [int(i) for i in input_list]
    except Exception:
        raise Exception("Input khong hop le! Input phai la so nguyen")
    a = []
    try:
        for _ in range(n):
            temp = input()
            temp_list = temp.split()
            if len(temp_list) != m:
                raise Exception("Input khong hop le! Input phai co m so nguyen tren 1 dong")
            try:
                input_col = [int(i) for i in temp_list]
                a.append(input_col)
            except:
                raise Exception("Input khong hop le! Input phai la so nguyen")
            
    except :
        raise Exception("Input khong hop le! Cac phan tu phai la so nguyen.")
    
    for i in range(n):
        for j in range(m):
            if a[i][j] not in primes:
                a[i][j] = 0
            else:
                a[i][j] = 1
            print(a[i][j], end = ' ')
        print()

if __name__ == '__main__':
    sieve(size)
    try:
        main()
    except Exception as e:
        print(e)