n,m=map(int,input().split())

board=[]

for _ in range(n):
    board.append(list(input()))

answer_w=[['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W']]

answer_b=[['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B'],
          ['B','W','B','W','B','W','B','W'],
          ['W','B','W','B','W','B','W','B']]

def check(i,j):
    for k in range(i, i + 7):
        for u in range(j, j + 7):
            if board[k][u] == 'W':
                if board[k + 1][u] != 'B' or board[k][u + 1] != 'B':
                    return False
            else:
                if board[k + 1][u] != 'W' or board[k][u + 1] != 'W':
                    return False
    return True

num_n=n-7
num_m=m-7

result=1e9

for i in range(num_n):
    for j in range(num_m):
        temp_1=0
        temp_2=0


        for k in range(i,i+8):
            for u in range(j,j+8):
                if board[k][u]!=answer_w[k-i][u-j]:
                    temp_1+=1

        for k in range(i, i + 8):
            for u in range(j, j + 8):
                if board[k][u] != answer_b[k - i][u - j]:
                    temp_2+=1

        result=min(result,temp_1,temp_2)

print(result)