
def check_num(l:list,n):
    l = sorted(l)
    for i in l:
        if n == i:
            n += 1
    l.append(n)
    return n

n = int(input())
day1 = dict()
for _ in range(n):
    adress = input()
    # from str to NAME and NUMBER of building
    s_name = ''.join(map(str,[i for i in adress if i.isalpha()]))
    s_dig = int(''.join(map(str,[i for i in adress if i.isdigit()])))
    v = []
    # fill dict of unique NAME plus list of number plates
    if s_name in day1:
        if s_dig not in day1.get(s_name):
            day1.get(s_name).append(s_dig)
    else:
        v.append(s_dig)
        day1[s_name] = v
# fill second day
m = int(input())
day2l = []
for _ in range(m):
    adress = input()
    day2l.append(adress)
f = []
if len(day1)==0:
    d2_new = []
    for i in day2l:
        if i in d2_new:
            count = d2_new.count(i)
            f.append(count + 1)
        else:
            count = 1
            f.append(count)
        d2_new.append(i)
else:
    for i in day2l:
        if i in day1:
            t = check_num(day1.get(i), 1)
            f.append(t)
            day1.get(i).append(t)
        else:
            f.append(1)
for i in f:
    print(i)
