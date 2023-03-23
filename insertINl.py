def check_num(l:list,n):
    for i in l:
        if n == i:
            n += 1
    l.append(n)
    return n

l = [1,6,4]
print(check_num(l, 1))
