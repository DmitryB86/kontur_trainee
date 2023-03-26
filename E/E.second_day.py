def get_num(s:set):
    n=1
    while True:
        while n in s:
            n+=1
        s.add(n)
        yield n

day1 = {'mira': {32, 1, 3, 4, 6, 12}, 'turgeneva': {2, 4, 6}}
#  second day
m = int(input())
for _ in range(m):
    adress = input()
    s = set()
    if adress in day1:
        get_num(day1[adress])
    else:
        day1[adress]=s
    t = get_num(day1[adress])
    print(next(t))

