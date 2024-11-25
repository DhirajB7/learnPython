car = {
    "color" : "red",
    "brand" : "audi",
    "wheels": 4,
    "you_kidding": False
}

print(len(car))
print(car.get("brand"))
print(car["brand"])
print(car.keys())
print(type(car.keys()))
print(list(car.keys()))
print(car.values())
print(type(car.values()))
print(list(car.values()))

print(car)
car.update({"wiper":True})
print(car)

print(car)
car.update({"you_kidding":True})
print(car)

print("===========================")

for x,y in car.items() :
    print(x,":",y)