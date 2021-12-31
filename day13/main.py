input = open("input.txt").read().splitlines()
instr_i = input.index('')
coords = list(map(lambda x: [int(n) for n in x.split(",")], input[:instr_i]))
instructions = [s.split('fold along ')[1].split('=') for s in input[instr_i+1:]]

def fold(x, y, coords):
    fold = x if x != 0 else y
    is_y = y!=0
    coords2 = [n for n in coords if n[1*is_y] >= fold]
    coords1 = [n for n in coords if n[1*is_y] < fold]
    for c in coords2:
        new_coord = c
        if y != 0:
            new_coord[1*is_y] = fold - (c[1*is_y]-fold)
        if x != 0:
            new_coord[1*is_y] = fold - (c[1*is_y]-fold)
        if new_coord not in coords1:
            coords1.append(new_coord)
    return coords1

for instr in instructions:
    if instr[0] == 'x':
        coords = fold(int(instr[1]), 0, coords)
    else:
        coords = fold(0, int(instr[1]), coords)

xmin = min(x for x, y in coords)
xmax = max(x for x, y in coords)
ymin = min(y for x, y in coords)
ymax = max(y for x, y in coords)
for y in range(ymin, ymax + 1):
    print("".join("#" if [x, y] in coords else "."
               for x in range(xmin, xmax + 1)))
