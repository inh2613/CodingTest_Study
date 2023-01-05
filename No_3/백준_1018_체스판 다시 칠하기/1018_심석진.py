# 홀짝으로도 할 수 있음
import sys

N,M = list(map(int, sys.stdin.readline().split()))
board = []

for _ in range(N):
    row = list(sys.stdin.readline().rstrip())
    board.append(row)

BW = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']
]

WB = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']
]

ans = 64

for x in range(N-7):
    for y in range(M-7):
        bb = 0
        ww = 0
        for i in range(8):
            for j in range(8):
                if board[x+i][y+j] != BW[i][j]: bb += 1
                if board[x+i][y+j] != WB[i][j]: ww += 1

        if bb < ans: ans = bb
        if ww < ans: ans = ww

print(ans)