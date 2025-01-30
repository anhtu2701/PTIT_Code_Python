import re
text = ""
while True:
    try:
        text += input()
    except EOFError:
        break
clean_text = re.split(r'[.?!]', text)
for line in clean_text:
    res = line.strip().lower().split()
    if res:
        res[0] = res[0].title()
        print(*res)