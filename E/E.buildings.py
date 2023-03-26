
def get_num(s:set):
    n=1
    while True:
        while n in s:
            n+=1
        yield n
        s.add(n)

# in first day
n = int(input())
day1=[]
for _ in range(n):
    day1.append(input())
day2=[]
m = int(input())
for _ in range(m):
    day2.append(input())


day1_d={}
for adress in day1:
    street_name = adress.rstrip('0123456789')
    building_number = int(adress[len(street_name):])
    s_p = day1_d.get(street_name)
    if not s_p:
        s_p = set()
        day1_d[street_name] = s_p
    day1_d[street_name].add(building_number)


street_gen={}
for street_name,gener in day1_d.items():
    street_gen[street_name]=get_num(gener)

for adress in day2:
    t = street_gen.get(adress)
    if not t:
        t = get_num(set())
        street_gen[adress]=t
    print(next(t))