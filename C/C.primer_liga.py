n = input()
d = dict()

control = []
# dfd

d_win = dict()
d_lose = dict()
d_equaly = dict()

for _ in range(int(n)):
    newstr = input()
    d[newstr.split(' ')[0]] = int(newstr.split(' ')[1])

# who_plays = input()
# comA = who_plays.split('-')[0]
# comB = who_plays.split('-')[1]
comA, comB = input().split('-')
# case win
d_win = d.copy()
d_win[comA]+=3
d_win = sorted(d_win.items(), key=lambda value: (-value[1],value[0]))
for i in d_win:
    if i[0]==comA:
        control.append(d_win.index(i)+1)
# print(d_win)

# case equaly
d_equaly = d.copy()
d_equaly[comA]+=1
d_equaly[comB]+=1
d_equaly = sorted(d_equaly.items(), key=lambda value: (-value[1],value[0]))
for i in d_equaly:
    if i[0]==comA:
        control.append(d_equaly.index(i)+1)
# print(d_equaly)

# case lose
d_lose = d.copy()
d_lose[comB]+=3
d_lose = sorted(d_lose.items(), key=lambda value: (-value[1],value[0]))
for i in d_lose:
    if i[0]==comA:
        control.append(d_lose.index(i)+1)
# print(d_lose)
print(*control)
