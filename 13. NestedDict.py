dad = {
    "name" : "appa",
    "gender":"boy"
}

mom = {
    "name" : "amma",
    "gender":"girl"
}

child = {
    "name" : "magu",
    "gender":"girl"
}

family = {
    "dad":dad,
    "mom":mom,
    "child":child
}

print(family)

for x in family.values():
    print(x.get('name'),"is a",x.get('gender'))