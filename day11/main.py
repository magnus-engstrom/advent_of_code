input = open("input.txt").read().splitlines()
octopuses = {}
for o in [[str(col) + '_' + str(row), int(number), int(col), int(row)] for row, line in enumerate(input) for col, number in enumerate(line)]:
    octopuses[o[0]] = [o[1], [
           str(o[2]-1) + '_' + str(o[3]),
           str(o[2]+1) + '_' + str(o[3]),
           str(o[2]) + '_' + str(o[3]-1),
           str(o[2]) + '_' + str(o[3]+1),
           str(o[2]-1) + '_' + str(o[3]+1),
           str(o[2]+1) + '_' + str(o[3]-1),
           str(o[2]-1) + '_' + str(o[3]-1),
           str(o[2]+1) + '_' + str(o[3]+1),
        ]
    ]
sum = 0
all_flashed = 0
for i in range (500):
    flashing = set()
    flashed = set()
    for key in octopuses.keys():
        octopuses[key][0] += 1
        if octopuses[key][0] > 9:
            flashing.add(key)
    while flashing:
        key = flashing.pop()
        octopuses[key][0] = 0
        flashed.add(key)
        for n in octopuses[key][1]:
            if n in octopuses.keys() and n not in flashed:
                octopuses[n][0] += 1
                if octopuses[n][0] > 9:
                    flashing.add(n)
    if len(flashed) == 100 and all_flashed == 0:
        all_flashed = i+1
    sum += len(flashed)
print("Day 11, part 1, answer:", sum)
print(all_flashed)