n = int(input())

l = [i for i in str(n)]
Maxs, Mins ='',''
Maximum = sorted(l, reverse=True)
Minimum = sorted(l)

for i in Maximum:
    Maxs+=str(int(i))

for j in Minimum:
    Mins+=str(int(j))
print(int(Maxs)- int(Mins))
