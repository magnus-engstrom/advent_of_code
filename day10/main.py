# input = open("chunks.txt").read().splitlines()
# lookup_table = {
#     '(': ')',
#     '{': '}',
#     '[': ']',
#     '<': '>',
# }
# points = {
#     ')': 3,
#     ']': 57,
#     '}': 1197,
#     '>': 25137 
# }
# sum = 0
# for row in input:
#     open_chars = ''
#     close_chars = ''
#     for char in row:
#         open_chars += char
#         if char in lookup_table.keys():
#             close_chars = lookup_table[char] + close_chars
#         elif char == close_chars[0]:
#             close_chars = close_chars[1:]
#         else:
#             sum += points[char]
#             break

# print(sum)

input = open("chunks.txt").read().splitlines()
lookup_table = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4 
}
scores = []
for row in input:
    corrupt = False
    open_chars = ''
    close_chars = ''
    for char in row:
        open_chars += char
        if char in lookup_table.keys():
            close_chars = lookup_table[char] + close_chars
        elif char == close_chars[0]:
            close_chars = close_chars[1:]
        else:
            corrupt = True
            break
    if not corrupt:
        score = 0
        for c in close_chars:
            score *= 5
            score += points[c]
        scores.append(score)
scores.sort()
mid = len(scores) // 2
answer = (scores[mid] + scores[~mid]) / 2
print(int(answer))