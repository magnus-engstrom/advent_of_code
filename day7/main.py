f = open("crabs.txt", "r")
crabs = [int(i) for i in f.read().split(',')]

crabs.sort()
mid = len(crabs) // 2
median = (crabs[mid] + crabs[~mid]) / 2
print(median)
fuel = 0
for c in crabs:
    fuel += abs(c-median)
print("Day 7, part 1, answer:", fuel)

f = open("crabs.txt", "r")
crabs = [int(i) for i in f.read().split(',')]
avg = int(sum(crabs)/len(crabs))
fuel = 0
for c in crabs:
    dist = abs(c-avg)
    fuel += sum(range(0, dist+1))
print("Day 7, part 2, answer:", fuel)