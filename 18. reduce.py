from functools import reduce

a = [x for x in range(1,6)]
print(a)

z = reduce(lambda  x,y:x+y,a)
print(z)