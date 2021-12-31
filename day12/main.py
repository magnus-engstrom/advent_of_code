# input = open('test.txt').read().splitlines()
# input = list(map(lambda x: x.split('-'), input))

# cave_links = {}

# for line in input:
#     if line[0] in cave_links.keys():
#         cave_links[line[0]] += [line[1]]
#     else:
#         cave_links[line[0]] = [line[1]]
#     if line[1] in cave_links.keys():        
#         cave_links[line[1]] += [line[0]]
#     else:
#         cave_links[line[1]] = [line[0]]

# def explore(visited=[], cave='start'):
#     if cave == 'end':
#         return 1
#     if cave in visited:
#         if cave.islower():
#             return 0
#     sum = 0
#     for n in cave_links[cave]:
#         sum += explore(visited+[cave], n)
#     return sum


# print("Day 12, part 1, answer:", explore())

input = open('input.txt').read().splitlines()
input = list(map(lambda x: x.split('-'), input))

cave_links = {}

for line in input:
    if line[0] in cave_links.keys():
        cave_links[line[0]] += [line[1]]
    else:
        cave_links[line[0]] = [line[1]]
    if line[1] in cave_links.keys():        
        cave_links[line[1]] += [line[0]]
    else:
        cave_links[line[1]] = [line[0]]

def explore(visited=[], cave='start', twice=False):
    if cave == 'end':
        return 1
    if cave in visited:
        if cave == 'start':
            return 0
        if cave.islower():
            if twice:
                return 0
            else:
                twice = True
    sum = 0
    for n in cave_links[cave]:
        sum += explore(visited+[cave], n, twice)
    return sum

print("Day 12, part 2, answer:", explore())