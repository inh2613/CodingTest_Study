# 체스판 다시 칠하기

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(input()))

board_starting_b = []
board_starting_w = []
for r in range(8):
    if r % 2 == 0:
        board_starting_b.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])
        board_starting_w.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])

    else:
        board_starting_b.append(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'])
        board_starting_w.append(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'])


min_fix = 64
for i in range(n-7):
    for j in range(m-7):
        fix_b = 0
        fix_w = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if g[x][y] != board_starting_b[x-i][y-j]:
                    fix_b += 1
                if g[x][y] != board_starting_w[x-i][y-j]:
                    fix_w += 1
        fix = min(fix_w, fix_b)

        if min_fix > fix:
            min_fix = fix

print(min_fix)