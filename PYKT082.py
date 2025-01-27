def convert_IELTS_score(n):
    if 40 >= n >= 39: return "9.0"
    elif n > 36: return "8.5"
    elif n > 34: return "8.0"
    elif n > 32: return "7.5"
    elif n > 29: return "7.0"
    elif n > 26:  return "6.5"
    elif n > 22: return "6.0"
    elif n > 19: return "5.5"
    elif n > 15: return "5.0"
    elif n > 12:  return "4.5"
    elif n > 9: return "4.0"
    elif n > 6: return "3.5"
    elif  n > 4: return "3.0"
    else: return "1.0"

def round_score(x):
    phay = x - int(x)
    if phay == 0.25:
        return int(x) + 0.5
    elif phay == 0.5:
        return int(x) + 1
    else:
        return round(x * 2) / 2
    
for i in range(int(input())):
    read, lis, speak_score, wri_score = map(float,input().split())
    read_score = float(convert_IELTS_score(read))
    lis_score = float(convert_IELTS_score(lis))
    average_score = round_score((read_score + lis_score + speak_score + wri_score) / 4)
    print('%.1f' % average_score)













