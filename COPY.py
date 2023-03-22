#
# s = 'mira32'
# s_name = ''
# name = [i for i in s if i.isalpha()]
# for i in name:
#     s_name+=i
# s_dig = ''
# dig = [i for i in s if i.isdigit()]
# for j in dig:
#     s_dig+=j
# print(s_name,s_dig)
#
# d = [('dict',1), ('dict',2)]
# print(d)

p = [('mira', 32), ('turgeneva', 4), ('mira', 1), ('turgeneva', 5), ('nobela', 4), ('turgeneva', 4)]

d = dict()
for i in p:
    v = []
    if i[0] in d:
        if i[1] not in d.get(i[0]):
            d.get(i[0]).append(i[1])
    else:
        v.append(i[1])
        d[i[0]] = v
print(d)