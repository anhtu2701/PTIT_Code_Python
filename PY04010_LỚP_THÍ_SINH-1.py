class Thisinh:
    def __init__(self, name, birthdate, score1, score2, score3):
        self.name = name
        self.bd = birthdate
        self.score = score1 + score2 + score3

    def __str__(self):
        return f"{self.name} {self.bd} {self.score}"
    
if __name__ == "__main__":
    name = input().title()
    birthdate = input()
    score1 = float(input())
    score2 = float(input())
    score3 = float(input())
    student = Thisinh(name, birthdate, score1, score2, score3)
    print(student)