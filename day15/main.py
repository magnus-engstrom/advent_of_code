input = open('input.txt').read().splitlines()
grid = [list(map(int, row)) for row in input]
mw, mh = (len(grid[0]), len(grid))

open_list = [(0,0,0)]
closed_list = {}

done = False
while not done:
    open_list = [(x, y, s) for x, y, s in open_list if (x, y) not in closed_list or closed_list[(x, y)] > s]
    open_list.sort(key=lambda x: x[2], reverse=True)
    x, y, score = open_list.pop()
    closed_list[(x, y)] = score
    for nx, ny in [(x+1, y), (x-1,y), (x, y+1), (x, y-1)]:
        if nx >= 0 and ny >= 0 and nx <= mw*5-1 and ny <= mh*5-1:
            calc_grid_score = grid[ny%mh][nx%mw]+int(nx/mh)+int(ny/mw)
            if calc_grid_score > 9:
                calc_grid_score -= 9
            open_list.append((nx, ny, score+calc_grid_score))
            if nx == mw*5-1 and ny == mh*5-1:
                print(score+calc_grid_score)
                done = True