a = [x for x in range(1,101)]
print(a)

def make_all_even(num) :
    if num % 2==1 :
        return num+1
    else :
        return num

b = list(map(make_all_even,a))
print(b)

c = list(map(lambda d:d*5,a))
print(c)