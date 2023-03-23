d1 = {}
d2 = ['mira','turgeneva','turgeneva','turgeneva','turgeneva','lenina','mira']
print(d2)
f = []
d2_new=[]
for i in d2:
    if i in d2_new:
        count=d2_new.count(i)
        f.append(count+1)
    else:
        count = 1
        f.append(count)
    d2_new.append(i)
print(f)