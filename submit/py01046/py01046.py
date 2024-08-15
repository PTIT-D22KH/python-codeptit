# py01046.py
def tower(n, source, helper, dest):
    if (n == 0):
        return
    tower(n - 1, source, dest, helper)
    print(f"{source} -> {dest}")
    tower(n - 1, helper, source, dest)
def main():
    # Write your code here
    n = int(input())
    tower(n, 'A', 'B', 'C')

if __name__ == '__main__':
    main()
