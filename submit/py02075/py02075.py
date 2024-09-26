# py02075.py
class Segment:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.end < other.end
    

    
def main():
    # Write your code here
    for _ in range(int(input())):
        n = int(input())
        a = []
        for _ in range(n):
            start, end = [int(i) for i in input().split()]
            a.append(Segment(start, end))
        a.sort()
        last = -1
        count = 0
        for x in a:
            if x.start >= last:
                count += 1
                last = x.end
        print(count)

if __name__ == '__main__':
    main()
