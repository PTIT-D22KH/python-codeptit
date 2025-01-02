# py03006.py
import re
class Word:
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre
    

def check(x):
    for a in x:
        if a.isdigit():
            return False
    return True


def main():
    # Write your code here
    d = {}
    for _ in range(int(input())):
        s = re.split("[^a-z]", input().lower())
        for x in s:
            if x != "":
                if check(x):
                    if x not in d:
                        d[x] = 1
                    else:
                        d[x] += 1
    res = sorted(d, key=lambda x:(-d[x], x))
    for x in res:
        print(f"{x} {d[x]}")
    


if __name__ == '__main__':
    main()
