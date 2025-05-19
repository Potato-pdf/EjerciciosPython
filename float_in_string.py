t = int(input()) 
for _ in range(t):
    n = input()
    try:
        float(n) 
        if "." in n:
            print(True) 
        else:
            print(False)
    except ValueError:
        print(False)

