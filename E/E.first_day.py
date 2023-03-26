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

    '''this is part through the dict without generator'''
    if street_name in day1:
        if building_number not in day1[street_name]:
            day1[street_name].add(building_number)
    else:
        s = set()
        s.add(building_number)
        day1[street_name] = s
    ''' '''
    # s = set()
    # s.add(building_number)
    # t = get_num(s)
    # day1[street_name] = t
    # # print(next(t))
print(day1)


