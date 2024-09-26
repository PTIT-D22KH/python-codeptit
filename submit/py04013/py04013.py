class Time:
    def __init__(self, time_str):
        self.hours, self.minutes = map(int, time_str.split(":"))

    def timeDiffToTotalMinutes(self, other):
        start_minutes = self.hours * 60 + self.minutes
        end_minutes = other.hours * 60 + other.minutes
        return end_minutes - start_minutes

    @staticmethod
    def minutesToHourDecimal(minutes):
        return minutes / 60.0

class Station:
    count = 0

    def __init__(self, name, startTime, endTime, rainVolume):
        self.name = name
        Station.count += 1
        self.id = f"T{Station.count:02d}"
        self.totalMinutes = self.calTotalMinutes(startTime, endTime)
        self.rainVolume = rainVolume
        self.averageRainVolume = 0.0

    def calTotalMinutes(self, startTime, endTime):
        start = Time(startTime)
        end = Time(endTime)
        return start.timeDiffToTotalMinutes(end)

    def calAverageRainVolume(self):
        self.averageRainVolume = self.rainVolume / Time.minutesToHourDecimal(self.totalMinutes)

    def getName(self):
        return self.name

    def updateRainVolume(self, newRainVolume):
        self.rainVolume += newRainVolume

    def addTime(self, startTime, endTime):
        self.totalMinutes += self.calTotalMinutes(startTime, endTime)

    def __str__(self):
        return f"{self.id} {self.name} {self.averageRainVolume:.2f}"

def main():
    n = int(input())
    stations = []
    station_map = {}

    for _ in range(n):
        name = input().strip()
        startTime = input().strip()
        endTime = input().strip()
        rainVolume = float(input().strip())

        if name not in station_map:
            station = Station(name, startTime, endTime, rainVolume)
            stations.append(station)
            station_map[name] = station
        else:
            station = station_map[name]
            station.addTime(startTime, endTime)
            station.updateRainVolume(rainVolume)

    for station in stations:
        station.calAverageRainVolume()

    for station in stations:
        print(station)

if __name__ == '__main__':
    main()