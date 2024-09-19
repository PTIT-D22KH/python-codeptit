def sieve(limit):
    a = [i for i in range(limit + 1)]
    i = 2
    while i * i <= limit:
        if a[i] == i:
            for j in range(i * i, limit + 1, i):
                if a[j] == j:
                    a[j] = i
        i += 1
    return a

def count_special_numbers(n):
    s = 0
    l = int(n ** 0.5)
    a = sieve(l)
    
    for i in range(2, l + 1):
        p = a[i]
        q = a[i // a[i]]
        if p * q == i and q != 1 and p != q:
            s += 1
        elif a[i] == i:
            if i ** 8 <= n:
                s += 1
    return s

def main():
    n = int(input())
    result = count_special_numbers(n)
    print(result)

if __name__ == '__main__':
    main()