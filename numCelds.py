def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    for i in range(n):
        for j in range(m):
            actual = grid[i][j]
            dominante = True

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] >= actual:
                        dominante = False
                        break

            if dominante:
                count += 1

    return count

n = int(input())  
m = int(input())  

grid = []
for _ in range(n):
    fila = list(map(int, input().split()))
    grid.append(fila)

print(numCells(grid))
