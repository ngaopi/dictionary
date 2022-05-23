def num(a):
    c=""
    i=0
    while i<len(a):
        if a[i].isnumeric():
            return c
        elif a[i] not in c:
            return a
    i=i+1
print(num("ring1232*!@"))