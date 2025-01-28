#Cho một số nguyên dương N không quá 5 chữ số, hãy kiểm tra và in ra số đó chẵn hay lẻ. Nếu chẵn ghi ra chữ CHAN, nếu ngược lại ghi ra chữ LE.
number = int(input())
if number % 2 == 0:
    print("CHAN")
else:
    print("LE")