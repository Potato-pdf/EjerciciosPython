import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return round(float(self.a * self.b), 2)

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return round(float(math.pi * self.r ** 2), 2)

t = int(input()) 
for _ in range(t):
    entrada = input()
    partes = entrada.split()

    if partes[0].lower() == "rectangle":
        a = int(partes[1])
        b = int(partes[2])
        figura = Rectangle(a, b)
    elif partes[0].lower() == "circle":
        r = int(partes[1])
        figura = Circle(r)
    else:
        continue 
    print(f"{figura.area():.2f}")
