m = 15
n = 15

matrix = [[0 for x in range(n)] for y in range(m)]

i = 0
j = 0

for i in range(m):
    for j in range(n):
        matrix[i][j] = 0
matrix[0][0] = 1
for count in range(1, m):
    i = count
    j = 0
    while (i >= 0) and (j < n):
        if i != 0:
            matrix[i][j] = matrix[i-1][j]
        if j != 0:
            matrix[i][j] += matrix[i][j-1]
        i -= 1
        j += 1
        if i == 0 and j == 1:
            matrix[i][j] = 1
count = 1
for count in range(1, n):
    i = m - 1
    j = count
    while j < n and i >= 0:
        if i != 0:
            matrix[i][j] = matrix[i - 1][j]
        if j != 0:
            matrix[i][j] += matrix[i][j - 1]
        i -= 1
        j += 1
for i in range(m):
    for j in range(n):
        print(str(matrix[i][j]), end=" ")
    print()
print()
print(str(matrix[m-1][n-1]))

