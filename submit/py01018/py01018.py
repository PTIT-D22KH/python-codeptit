# py01018.py

def main():
    # Write your code here
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    word_dict = {}
    for i, char in enumerate(p):
        # print(i, char)
        word_dict[char] = i
    # print(word_dict)
    while(True):
        s = input()
        l = s.split()
        # print(len(l))
        if (len(l) == 1):
            break
        k, b = [i for i in l]
        k = int(k)
        # print(k)
        res = ""
        for i in range(len(b)):
            idx = (word_dict[b[i]] + k) % 28
            # print(idx)
            c = p[idx]
            res = res + c

        # print(res)
        res = res[::-1]
        # res = b[-1:0:-1]
        print(res)



        

if __name__ == '__main__':
    main()
