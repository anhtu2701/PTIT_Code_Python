class Gamer:
    def __init__(self, id, name, timeIn, timeOut):
        self.id = id
        self.name = name.title()
        self.timeIn = timeIn
        self.timeOut = timeOut
        self.time = self.calculateTime()

    def calculateTime(self):
        i = int(self.timeIn[:2]) * 60 + int(self.timeIn[3:])
        o = int(self.timeOut[:2]) * 60 + int(self.timeOut[3:])
        return o - i

    def strTime(self):
        hour = self.time // 60
        minute = self.time % 60
        return f"{hour} gio {minute} phut"
    
    def __str__(self):
        return f"{self.id} {self.name} {self.strTime()}"
    
if __name__ == "__main__":
    n = int(input())
    gamers = []
    for i in range(n):
        id = input()
        name = input()
        timeIn = input()
        timeOut = input()
        gamers.append(Gamer(id, name, timeIn, timeOut))
    gamers.sort(key=lambda x: -x.time)
    for gamer in gamers:
        print(gamer)