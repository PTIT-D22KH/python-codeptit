

def main():
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    
    d = [0] * (m + 1)
    for x in a:
        d[x]+= 1
    max_value = max(d)
    for x in range(1, m + 1):
        if d[x] == max_value:
            d[x] = 0
    res = max(d)
    if (d.index(res)):
        print(d.index(res))
    else:
        print("NONE")
    # print(d.index(res) if res else "NONE")

if __name__ == '__main__':
    main()