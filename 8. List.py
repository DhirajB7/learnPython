lis = ["apple","banana","grapes","apple"]
print(len(lis))
print(lis)
print(type(lis))

csv_data = "nishi,kishor,mayank,dhiraj"
lis2 = csv_data.split(",")
print(lis2[-3:])
print("dhiraj" not in lis2)
lis2.insert(2,"saksham")
print(lis2)
lis2.append("yshika")
print(lis2)
lis.extend(lis2)
print(lis)
print("===","looping shorthand","====")
[print(x) for x in lis]