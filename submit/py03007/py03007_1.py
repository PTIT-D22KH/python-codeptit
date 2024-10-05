# py03007.py
import re
def main():
    # Write your code here
    s = ""
    
    # regex = r'[(\w)]+' # tach tu
    # regex = r'[\w]+'# cung la tach tu
    regex = r'[\w\s\,\:]+'
    # split_regex = r'[\.\?\!]+'
    while True:
        try:
            s += input()
        except Exception:
            break
    s = re.findall(regex, s)
    # print(s)


    # a = re.split(split_regex, s)
    # print(a)


    for i in s:
        x = i.strip().lower().split()
        if (len(x) == 0):
            continue
        # print(x)
        x[0] = x[0].title()
        curr = 0
        for curr in x:
            j = 0
            while j < len(curr):
                if not curr[j].isalnum():
                    j += 1
                else:
                    break
            curr = curr[j:]
            # print(curr.split())
            if (len(curr.split()) == 0):
                # print(curr.split())
                continue
            
            print(curr, end = ' ')
        print()
        # print(" ".join(x))




if __name__ == '__main__':
    main()
