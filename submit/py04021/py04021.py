# py04021.py
class Time:
    def __init__(self, *args) -> None:
        if (len(args) == 1):
            timeString = args[0]
            a = timeString.split(":")
            self.hour = int(a[0])
            self.minutes = int(a[1])
        elif (len(args) == 2):
            self.hour = args[0]
            self.minutes = args[1]
    def  timeDiff(self, other):
        x = other.hour - self.hour
        y = other.minutes - self.minutes
        if (y < 0):
            y += 60
            x -= 1
        return Time(x, y)
    def hourToMinutes(self):
        return self.hour * 60 + self.minutes
    def __str__(self) -> str:
        return str(self.hour) + " gio " + str(self.minutes) + " phut"
class Gamer:
    def __init__(self, id, name, inString, outString) -> None:
        self.id = id
        self.name = name
        self.inTime = Time(inString)
        self.outTime  = Time(outString)
        self.playingTime = self.inTime.timeDiff(self.outTime)
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + str(self.playingTime)

def cmp(a):
    return (-a.playingTime.hourToMinutes())

        
def main():
    # Write your code here
    n = int(input())
    a = []
    for _ in range(n):
        a.append(Gamer(input(), input(), input(), input()))
    a.sort(key = cmp)
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()
