# week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# days = ((i, week[(i + 4) % 7]) for i in range(1, 78))
# print(next(days))

# for i in range(1,20):
#     print(i%7, ' ',i%8,' ',i%9 )
import sys

def genf():
    for i in range(1,20000000):
        yield i
def genf1():
    for i in range(1,20000000):
        print(i)

print(genf1())
print(sys.getsizeof(genf()))
print('*'*10)
print(sys.getsizeof(genf1()))
