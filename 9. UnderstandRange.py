lis = [x for x in range(1,101)]
lis2 = [str(x) for x in range(1,101)]
print(lis)
print(lis2)
thislist = ["orange", "Mango", "kiwi", "Pineapple", "banana"]
thislist.sort(key=str.lower)
print(thislist)
thislist2 = [100, 50, 65, 82, 23,1,11,10]
thislist2.sort(reverse=True)
print(thislist2)
print(thislist2*2)