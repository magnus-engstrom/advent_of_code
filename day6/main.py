# f = open("fishes.txt", "r")
# fishes = [int(i) for i in f.read().split(',')]
# for i in range(1,81):
#     new_fishes = 0
#     for fi in range(len(fishes)):
#         fishes[fi] -= 1
#         if fishes[fi] < 0:
#             fishes[fi] = 6
#             new_fishes += 1
#     fishes += [8]*new_fishes
# print("Day 6, part 1, answer:", len(fishes))

f = open("fishes.txt", "r")
fishes = [int(i) for i in f.read().split(',')]
fish_per_day = []
for i in range(7):
    count = 0
    for fish in fishes:
        if fish == i:
            count += 1
    fish_per_day.append(count) 

child_fishes = [0,0] 
for d in (range(256)):
    parent_fishes = fish_per_day[0] 
    child_fishes = child_fishes + [parent_fishes] 
    fish_per_day = fish_per_day[1:]+[parent_fishes] 
    fish_per_day[-1] += child_fishes[0] 
    child_fishes = child_fishes[1:]
answer = sum(fish_per_day)+sum(child_fishes)
print("Day 6, part 2, answer:", answer)