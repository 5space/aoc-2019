with open("input.txt", "r") as file:
    f = list(map(int, file.read().split(",")))

for n in range(len(f)):
    for m in range(len(f)):
        field = f.copy()
        field[1] = n
        field[2] = m
        c = 0
        while field[c] != 99:
            if field[c] == 1:
                a1, a2, a3 = field[c+1], field[c+2], field[c+3]
                field[a3] = field[a1] + field[a2]
            elif field[c] == 2:
                a1, a2, a3 = field[c+1], field[c+2], field[c+3]
                field[a3] = field[a1] * field[a2]
            c += 4
        if field[0] == 19690720:
            print(n, m)