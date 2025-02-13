class Hoadon:
    def __init__(self, id, name, old, new):
        self.id = id
        self.name = name
        self.change = new - old
        self.money = self.cal_money()

    def cal_money(self):
        if self.change <= 50:
            total = self.change * 100 * 1.02
        elif self.change <= 100:
            total = (5000 + (self.change - 50) * 150) * 1.03
        else:
            total = (12500 + (self.change - 100) * 200) * 1.05
        return round(total)
        
    def __lt__(self, other):
        return -self.change < -other.change
    
    def __str__(self):
        return(f"{self.id} {self.name} {self.money}")
    
if __name__ == "__main__":
    n = int(input())
    people = []
    for i in range(1,n+1):
        id = f"KH{i:02}"
        name = input().title()
        old = int(input())
        new = int(input())
        people.append(Hoadon(id, name, old, new))
    people.sort()
    for person in people:
        print(person)
            
    


    