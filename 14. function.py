def hello_world():
    print("hello function world")

hello_world()

#============================

def hello_name(name):
    print("hello function world my name is",name)

hello_name('Dhiraj')

#============================

def hello_loop(*data) :
    for x in list(data):
        print(x)

hello_loop([str(x) for x in range(1,11)],[str(x) for x in range(1,11)],[str(x) for x in range(1,11)])

#============================