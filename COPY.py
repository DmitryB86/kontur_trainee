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

# p = [('mira', 32), ('turgeneva', 4), ('mira', 1), ('turgeneva', 5), ('nobela', 4), ('turgeneva', 8)]
#
# d = dict()
# for i in p:
#     v = []
#     if i[0] in d:
#         if i[1] not in d.get(i[0]):
#             d.get(i[0]).append(i[1])
#     else:
#         v.append(i[1])
#         d[i[0]] = v
# print(d)

def check_num(l:list,n):
    l = sorted(l)
    for i in l:
        if n == i:
            n += 1
    l.append(n)
    return n

d1 = {'mira': [32, 2, 6, 3, 12, 15, 4], 'turgeneva': [3]}
# d1 = {}
d2list = ['mira','turgeneva','turgeneva','turgeneva','turgeneva','lenina','mira']

f = []
if len(d1)==0:
    d2_new = []
    for i in d2list:
        if i in d2_new:
            count = d2_new.count(i)
            f.append(count + 1)
        else:
            count = 1
            f.append(count)
        d2_new.append(i)
else:
    for i in d2list:
        if i in d1:
            t = check_num(d1.get(i),1)
            f.append(t)
            d1.get(i).append(t)
        else:
            f.append(1)

# for i in f:
#     if type(i) is list:
#         for j in i:
#             print(j)
#     else:
#         print(i)
print(f)