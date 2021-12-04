lines_data = open('instructions.txt', 'r').readlines()
agg_values = {
    'forward': 0,
    'up': 0,
    'down': 0
}
for line in lines_data:
    key, value = line.split(' ')
    agg_values[key] += int(value)
answer = agg_values['down']-agg_values['up']
answer *= agg_values['forward']
print("Day 2, part 1, answer:", answer)

aim = 0
depth = 0
distance = 0
for line in lines_data:
    key, value = line.split(' ')
    value = int(value)
    if 'forward' == key:
        distance += value
        depth += value * aim
        continue
    aim += value if 'down' == key else -value
print("Day 2, part 2, answer:", depth*distance)
