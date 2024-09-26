# py03007.py
import re
def main():
    # Write your code here
    s = ""
    regex = r'[\w\s,:]+'
    while True:
        try:
            s += input()
        except Exception:
            break
    s = re.findall(regex, s)
    for i in s:
        x = i.strip().lower().split()
        x[0] = x[0].title()
        print(" ".join(x))




if __name__ == '__main__':
    main()
