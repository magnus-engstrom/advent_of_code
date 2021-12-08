line_data = [l.replace('\n','').split(' -> ') for l in open('lines.txt', 'r').readlines()]
line_coords = list(map(lambda x: [list(map(int, l.split(','))) for l in x], line_data))
points = [[0]*1000 for _ in range(1000)]
diagonal_line_coords = []
for coordinate in line_coords:
    [[x1, y1], [x2, y2]] = coordinate
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            points[y1][x] += 1
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            points[y][x1] += 1
    if x1 != x2 and y1 != y2:
        diagonal_line_coords.append(coordinate)

flat_points = [col for row in points for col in row]            
print("Day 5, part 1, answer:", len(list(filter(lambda v: v > 1, flat_points))))

for coordinate in diagonal_line_coords:
    [[x1, y1], [x2, y2]] = coordinate
    x_step = 1 if x1 < x2 else -1
    y_step = 1 if y1 < y2 else -1
    x = x1
    y = y1
    for i in range(abs(x1-x2)+1):
        points[y][x] += 1
        x += x_step
        y += y_step

flat_points = [col for row in points for col in row]            
print("Day 5, part 2, answer:", len(list(filter(lambda v: v > 1, flat_points))))
