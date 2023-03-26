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
    # from str to NAME and NUMBER of building
    street_name = ''.join((i for i in adress if i.isalpha()))
    building_number = int(adress[len(street_name):])
    # fill dict of unique NAME plus list of number plates
    if street_name in day1:
        pass
    else:
        s = set()
        t = get_num(s)
        s.add(building_number)
        day1[street_name] = t

print(day1)
street_gen = {}
for street_name,plates in day1.items():
    street_gen[street_name] = get_num(plates)
t = street_gen['mira']
print(street_gen)
print(next(t))

#  second day
# m = int(input())
# day2 = {}
# for _ in range(m):
#     adress = input()
#     if adress in street_gen:
#         pass
#     else:
#         s = set()
#         street_gen[adress]=get_num(s)
#     t = get_num(s)
#     print(next(t))
