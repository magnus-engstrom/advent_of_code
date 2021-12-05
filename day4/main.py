bingo_data = [row.replace('\n', '') for row in open('bingo.txt', 'r').readlines()]
numbers = [int(n) for n in bingo_data[0].split(',')]
def check_board(board_numbers, bingo_numbers):
    rows = []
    counter = 0
    for i in range(0, len(board_numbers), 5):
        rows.append(board_numbers[i:i+5])
    cols = [[int(row[i]) for row in rows] for i in range(5)]
    for n in bingo_numbers:
        for i, row in enumerate(rows):
            if n in row:
                board_numbers = list(filter(lambda x: x != n, board_numbers))
                rows[i] = list(filter(lambda x: x != n, rows[i]))
                if len(rows[i]) == 0:
                    return counter, sum(board_numbers)*n
        for i, col in enumerate(cols):
            if n in col:
                board_numbers = list(filter(lambda x: x != n, board_numbers))
                cols[i] = list(filter(lambda x: x != n, cols[i]))
                if len(cols[i]) == 0:
                    return counter, sum(board_numbers)*n
        counter += 1     
    return

batch_size = 6
fastest_bingo = float('inf')
answer1 = 0

last_bingo = 0
answer1 = 0

for i in range(1, len(bingo_data), batch_size):
    board = []
    for l in bingo_data[i+1:i+batch_size]:
        for n in list(filter(lambda x: x != ' ' and x != '', l.split(' '))):
            board.append(int(n))
    bingo_at, board_sum = check_board(board, numbers)
    if bingo_at < fastest_bingo:
        fastest_bingo = bingo_at
        answer1 = board_sum
    if bingo_at >= last_bingo:
        last_bingo = bingo_at
        answer2 = board_sum
print("Day 4, part 1, answer:", answer1)
print("Day 4, part 2, answer:", answer2)