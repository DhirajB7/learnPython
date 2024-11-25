set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 | set2
set4 = set1 & set2
set5 = set1 - set2
set6 = set1 ^ set2
print("union",set3)
print("intersection",set4)
print("difference",set5)
print("symetrical_difference",set6)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) # <=
print(z)

x1 = {"f", "e", "d", "c", "b", "a"}
y1 = {"a", "b", "c"}
z1 = x.issuperset(y1) # >=
print(z1)