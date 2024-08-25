def main():
    while True:
        a = [int(i) for i in input().split()]
        b = [0] * 4
        if a == b:
            return
        count = 0
        while len(set(a)) > 1:
            new_a = [0] * 4
            for i in range(4):
                new_a[i] = abs(a[i] - a[(i + 1) % 4])
            a = new_a
            count += 1
        print(count)

if __name__ == '__main__':
    main()