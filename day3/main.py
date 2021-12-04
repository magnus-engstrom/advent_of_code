binaries = open('binaries.txt', 'r').readlines()
binaries = [r.replace('\n','') for r in binaries]
pivot_binaries = [[int(row[i]) for row in binaries] for i in range(12)]
gamma = ''
for i in range(12):
    gamma += str(max(pivot_binaries[i], key = pivot_binaries[i].count))
answer = int(gamma, 2) * (int(gamma, 2) ^ 0b111111111111)
print("Day 3, part 1, answer:", answer)

def value_by_position(arr, i, inverted=False):    
    value = ''.join([row[i] for row in arr])
    if inverted:
        return '1' if value.count('1') < value.count('0') else '0'
    else:
        return '1' if value.count('1') >= value.count('0') else '0'

oxygen = [*binaries]
co2 = [*binaries]
for i in range(len(binaries[0])):
    if len(oxygen) > 1:
        most = value_by_position(oxygen, i)
        oxygen = list(filter(lambda x: x[i] == most, oxygen))
    if len(co2) > 1:
        least = value_by_position(co2, i, True)
        co2 = list(filter(lambda x: x[i] == least, co2))

answer = int(oxygen[0], 2) * int(co2[0], 2)
print("Day 3, part 2, answer:", answer)