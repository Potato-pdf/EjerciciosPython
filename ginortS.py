s = input()

def sorted_key(c):
    return (c.isdigit(), c.isupper(), c.lower())

def es_par(c):
    return c.isdigit() and int(c) % 2 == 0

def custom_sort(c):
    return (es_par(c), sorted_key(c))

o = sorted(s, key=custom_sort)
print("".join(o))
