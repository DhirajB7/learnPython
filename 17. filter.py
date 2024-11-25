a = [x for x in range(1,101)]
print(a)

b = list(filter(lambda x:x%2==0,a))
print(b)

c = list(filter(lambda x:x%2==1,a))
print(c)