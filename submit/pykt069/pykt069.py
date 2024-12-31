# pykt069.py
from datetime import datetime
class Schedule:
    count = 0
    def __init__(self, timeString, start, room):
        Schedule.count += 1

        self.id = f"C{Schedule.count:03d}"
        self.time = datetime.strptime(timeString, '%d/%m/%Y')
        self.start = datetime.strptime(start, '%H:%M')
        self.totalTime = datetime.strptime(timeString + " " + start, '%d/%m/%Y %H:%M')
        self.room = room
    def __str__(self):
        return self.id + " " + datetime.strftime(self.time, '%d/%m/%Y') + " " + datetime.strftime(self.start, '%H:%M') + " " + self.room

def cmp(a):
    return (a.totalTime, a.id)

        
def main():
    # Write your code here
    a = []
    with open("CATHI.in", 'r') as file:
        input = file.readlines()
        curr = 1
        for _ in range(int(input[0])):

            # print(input[curr].split()[0])
            x = Schedule(input[curr].split()[0], input[curr + 1].split()[0], input[curr + 2].split()[0])
            # print(str(x))
            a.append(x)
            curr += 3
        a.sort(key = cmp)
        for x in a:
            print(str(x))

if __name__ == '__main__':
    main()
