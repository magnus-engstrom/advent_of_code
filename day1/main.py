depths = list(map(int, open('depths.txt', 'r').readlines()))
depth_increases = 0
for i in range(1, len(depths)):
    depth_increases += depths[i] > depths[i-1]
print("Day 1, part 1, answer:", depth_increases)

depth_increases = 0
for i in range(1, len(depths)-2):
    depth_increases += sum(depths[i-1:i+2]) < sum(depths[i:i+3])
print("Day 1, part 2, answer:", depth_increases)