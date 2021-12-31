heightmap = open("heightmap.txt").read().splitlines()

sum = 0
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        value = heightmap[y][x]
        compare = []
        for cy, cx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if y+cy >= 0 and y+cy < len(heightmap):
                if x+cx >= 0 and x+cx < len(heightmap[y]):
                    compare.append(heightmap[y+cy][x+cx])
        if value < min(compare):
            sum += int(value)+1
print("Day 9, part 1, answer:", sum)

heightmap = open("heightmap.txt").read().splitlines()
compare = []
basin_start = []
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        compare = []
        value = heightmap[y][x]
        for cy, cx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if y+cy >= 0 and y+cy < len(heightmap):
                if x+cx >= 0 and x+cx < len(heightmap[y]):
                    compare.append(heightmap[y+cy][x+cx])
        if value < min(compare):
            basin_start.append([y, x])

basin_areas = []
for start_point in basin_start:
    search_points = [start_point]
    basin_areas.append([])
    while len(search_points) > 0:
        p = search_points.pop()
        if p not in basin_areas[-1]:
            y, x = p
            basin_areas[-1].append(p)
            if y-1 >= 0 and heightmap[y-1][x] != '9':
                search_points.append([y-1, x])
            if y+1 < len(heightmap) and heightmap[y+1][x] != '9':
                search_points.append([y+1, x])
            if x-1 >= 0 and heightmap[y][x-1] != '9':
                search_points.append([y, x-1])
            if x+1 < len(heightmap[0]) and heightmap[y][x+1] != '9':
                search_points.append([y, x+1])
basin_areas.sort(key=lambda x: len(x), reverse=True)
answer = len(basin_areas[0])*len(basin_areas[1])*len(basin_areas[2])

print("Day 9, part 2, answer:", answer)