# Challenge with *args many positional arguments

def add(*args):
    suma = 0
    for n in args:
        suma += n
    return suma

print(add(1,1,1,1,1))

# Challenge with **Kwargs many key word arguements