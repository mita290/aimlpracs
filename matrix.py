matrix = []

value = 2

for i in range(4):
    row = []
    for j in range(3):
        row.append(value)
        value += 1
    matrix.append(row)

for row in matrix:
    print(row)
