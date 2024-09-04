class Time:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            s = args[0]
            self.hours, self.minutes = map(int, s.split(":"))
        elif len(args) == 2:
            self.hours, self.minutes = args

    def hourToMinutes(self):
        return self.hours * 60 + self.minutes

    def timeDiff(self, other):
        x = other.hours - self.hours
        y = other.minutes - self.minutes
        if y < 0:
            y += 60
            x -= 1
        return Time(x, y)

class Station:
    def __init__(self, name, startTime, endTime, rainVolume) -> None:
        self.name = name
        self.rainVolume = rainVolume
        start = Time(startTime)
        end = Time(endTime)
        self.duration = start.timeDiff(end).hourToMinutes()

    def calAverageRainVolume(self):
        self.avgVolume = self.rainVolume / self.duration

    def updateRainVolume(self, newVolume):
        self.rainVolume += newVolume
    
    def updateTime(self, startTime, endTime):
        start = Time(startTime)
        end = Time(endTime)
        self.duration += start.timeDiff(end).hourToMinutes()

    def __str__(self):
        return f"{self.name} {self.avgVolume:.2f}"

def main():
    n = int(input())
    a = []
    for _ in range(n):
        name = input()
        notFound = True
        startTime = input()
        endTime = input()
        newVolume = float(input())
        for x in a:
            if x.name == name:
                notFound = False
                x.updateTime(startTime, endTime)
                x.updateRainVolume(newVolume)
                break
        if notFound:
            a.append(Station(name, startTime, endTime, newVolume))
    for x in a:
        x.calAverageRainVolume()
    for x in a:
        print(str(x))

if __name__ == '__main__':
    main()