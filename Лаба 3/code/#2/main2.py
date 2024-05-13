from tabulate import tabulate
m = [" ", 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л']
n = ['00000000', '00000111', '00011001', '11000001', '01010101', '10110010', '10100100', '11111111']
table = []

for i in range(0, len(n)):
    line = [m[i + 1]]
    for l in range(0, i):
        line.append(" ")
    line.append("-")
    for j in range(i + 1, len(n)):
        num = 0
        for k in range(0, len(n[i])):
            if n[i][k] != n[j][k]:
                num += 1
        line.append(str(num))
    table.append(line)
print(tabulate(table, m, tablefmt="psql", numalign='center'))
