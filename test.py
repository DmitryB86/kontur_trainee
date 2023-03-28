n = int(input())

l = (int(i) for i in input().split())
d = {k:v for k,v in enumerate(l,1)}

# lmin = ((k,v) for k,v in d.items() if v==min(d.values()))
lmin = [k for k,v in d.items() if v==min(d.values())]
# lmax = ((k,v) for k,v in d.items() if v==max(d.values()))
lmax = [k for k,v in d.items() if v==max(d.values())]

minmin = min(lmin)
minmax = max(lmin)
maxmin = min(lmax)
maxmax = max(lmax)
if abs(minmin-maxmax)>abs(minmax-maxmin):
    print(min(minmin,maxmax),max(minmin,maxmax))
else:
    print(min(minmax,maxmin),max(minmax,maxmin))

