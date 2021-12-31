# input = open('input.txt').read().splitlines()
# template = input[0]
# rules = dict(r.split(' -> ') for r in input[2:])
# for step in range(10):
#     new_str = ''
#     old_c = ''
#     for i, c in enumerate(template):
#         pair = old_c + c 
#         new_str += old_c + rules[pair] if pair in rules.keys() else old_c
#         old_c = c
#     template = new_str+template[-1]
# occurances = [[template.count(c), c] for c in set(template)]
# occurances.sort(key=lambda x: x[0], reverse=True)
# print("Day 14, part 1, answer:", occurances[0][0]-occurances[-1][0])

input = open('test.txt').read().splitlines()
tpl = input[0]
rules = dict(r.split(' -> ') for r in input[2:])
pairs = dict([tpl[i]+tpl[i+1],1] for i in range(len(tpl)-1))
chars = {}
for _ in range(10):
    tp = pairs.copy()
    for k, v in pairs.items():
        if v > 0:
            nc = rules[k]
            tp[k] -= v
            if k[0]+nc not in pairs.keys():
                tp[k[0]+nc] = 0
            if nc+k[1] not in pairs.keys():
                tp[nc+k[1]] = 0
            tp[k[0]+nc] += v
            tp[nc+k[1]] += v
    pairs = tp
print(pairs)
l = {x: 0 for x in set(''.join(pairs.keys()))}
for k, v in pairs.items():
    l[k[0]] += v/2
    l[k[1]] += v/2
print(l)
# print(l)
# for i in range(9):
#     added_pairs = []
#     for k in pairs.keys():
#         added_pairs.append(k[0]+rules[k])
#         added_pairs.append(rules[k]+k[1])
#         chars += [k[0], rules[k], k[1]]
#         pairs[k] = 0
#     print(i)
# #print(pairs, chars)
# for c in chars:
#     count = 0
#     for k in pairs.keys():
#         if c in k:
#             count += pairs[k]
#     print(c, count)

data =  open('input.txt').read().splitlines()
s = data[0]
d = {i[:2] : i[-1] for i in data[2:]}

c = {k: s.count(k) for k in d.keys()}

for i in range(40):
    c2 = c.copy()
    for k, v in c.items():
        if c[k] > 0 :
            c2[k] -= v
            c2[k[0] + d[k]] += v
            c2[d[k] + k[1]] += v
    c = c2
l = {x: 0 for x in set(''.join(c.keys()))}

for k, v in c.items():
    l[k[0]] += v/2
    l[k[1]] += v/2
print(int(max(l.values()) - min(l.values())))
