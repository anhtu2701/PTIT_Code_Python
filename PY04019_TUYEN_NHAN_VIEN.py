def Phanloai(score):
    if score > 9.5: return "XUAT SAC"
    elif score >= 8: return "DAT"
    elif score >= 5 : return "CAN NHAC"
    else: return "TRUOT"

def Chuanhoa(score):
    if score > 10: return Phanloai(score / 10)
    else: return Phanloai(score)

class Thisinh:
    def __init__(self,id, name, score_lt, score_th):
        self.id = id
        self.name = name.title()
        self.score = (score_lt + score_th) / 2
        if self.score > 10:
            self.score = round(self.score / 10,2)
        else:
            self.score = round(self.score,2)
        self.res = Chuanhoa(self.score)

    # def __lt__(self, other):
    #     return -self.score < -other.score
    
    def __str__(self):
        return f"{self.id} {self.name} {self.score:.2f} {self.res}"

n = int(input())
people = []    
for _ in range(1, n+1):
    id = f"TS0{_}"
    name = input()
    score_lt = float(input())
    score_th = float(input())
    people.append(Thisinh(id, name, score_lt, score_th))
people.sort(key=lambda x: -x.score)
for person in people:
    print(person)

