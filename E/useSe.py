def get_from_set(s:set):
    num = 1
    while True:
        while num in s:
            num += 1
        yield num
        s.add(num)

s = {32, 1, 6, 3, 12, 15, 4}
t = get_from_set(s)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))