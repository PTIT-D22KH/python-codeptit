def main():
    s = ""
    
    while True:
        try:
            s += input()
        except Exception:
            break

    words = []
    word = ""
    for char in s:
        if char.isalnum() or char in [' ', ',', ':']:
            word += char
        else:
            if word:
                # print(word)
                words.append(word)
                word = ""
    if word:
        words.append(word)

    # print(words)

    for i in words:
        ok = True
        x = i.strip().lower().split()
        if len(x) == 0:
            continue
        x[0] = x[0].title()
        for curr in x:
            j = 0
            while j < len(curr):
                if not curr[j].isalnum():
                    j += 1
                else:
                    break
            curr = curr[j:]
            # print(len(curr))
            if len(curr.split()) == 0:
                ok = False
                break

            print(curr, end=' ')
        # print(len(x))
        if ok:
            print()

if __name__ == '__main__':
    main()