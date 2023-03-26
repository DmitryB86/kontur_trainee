n,m = map(int, input().split())
field = []
for i in range(n):

    for j in range(m):
        row = map(str, input().split())
        row.append(input())
    field.append(row)
    # for j in range(4):
    #     row = input()
    # field.append(row)

for i in field:
    print(i)
# for i in field:
#     print(i, end='')
