t = input()
p = input()
x=True
for i in range(0, len(t) - len(p)+1):
    x=True
    for j in range(i, len(p) + i):
        if p[j - i] != t[j]:
            x = False
            break
    if x == True:
        print(i)
