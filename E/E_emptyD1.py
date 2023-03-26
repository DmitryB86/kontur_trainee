def get_num(s:set):
    n=1
    while True:
        while n in s:
            n+=1
        yield n
        s.add(n)
# in first day
n = int(input())
day1 = dict()
for _ in range(n):
    adress = input()
    street_name = adress.rstrip('0123456789')
    building_number = int(adress[len(street_name):])
    if street_name not in day1:
        s = set()
        s.add(building_number)
        day1[street_name] = s
    else:
        day1[street_name].add(building_number)

street_gen = {}
for street_name,gener in day1.items():
    street_gen[street_name] = get_num(gener)

m = int(input())
for _ in range(m):
    adress = input()
    if adress not in street_gen:
        s = set()
        street_gen[adress]=get_num(s)
    t = street_gen[adress]
    print(next(t))
