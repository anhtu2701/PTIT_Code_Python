a = set()
with open ("CONTACT.in", "r", encoding = 'utf-8') as file:
    for i in file:
        a.add(i.strip().lower())
for x in sorted(a):
    print(x)