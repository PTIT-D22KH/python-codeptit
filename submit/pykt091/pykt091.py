# pykt091.py
class Word:
    count = 0
    def __init__(self, word, fre) -> None:
        self.id = Word.count
        Word.count += 1
        self.word = word
        self.fre = fre
    def __str__(self) -> str:
        return self.word + " " + str(self.fre)

def isPalindrome(s):
    return s[::-1] == s
def cmp(a):
    return (-len(a.word), a.id)
def main():
    # Write your code here
    # with open("pykt091/VANBAN.in", "r") as file:
    with open("VANBAN.in", "r") as file:
        a = []
        while True:
            s = file.readline().strip()
            if not s:
                break
            temp = s.split()
            for s in temp:
                if isPalindrome(s):
                    found = False
                    for w in a:
                        if w.word == s:
                            w.fre += 1
                            found = True
                            break
                    if not found:
                        a.append(Word(s, 1))
        a.sort(key = cmp)
        res = len(a[0].word)
        for x in a:
            if len(x.word) == res:
                print(str(x))

if __name__ == '__main__':
    main()
