#version1
from collections import deque

colas = deque()
colas.append(1)
colas.append(2)
colas.popleft()
print(colas)


#version 2
colas1 = []
colas1.append(1)
colas1.append(2)
colas1.append(3)

colas1.pop(0)
print(colas1)
