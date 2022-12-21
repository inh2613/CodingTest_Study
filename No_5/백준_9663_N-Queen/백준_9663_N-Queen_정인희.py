n = int(input())

board = [[0] * n for _ in range(n)]
visited = [False] * n

result = []


cnt=0


def dfs(depth):
    global cnt
    global result
    if depth == n:

        cnt+=1
        # print(result)
        # print('depth==n')
        return

    else:
        for i in range(n):
            if check(result, i) == False:
                if visited[i] == False:
                    visited[i] = True
                    result.append(i)
                    dfs(depth + 1)

                print('i',i)
                visited[i] = False
                result.pop()


def check(result,p):
    if p in result:
        return True
    for i in range(len(result)):
        if len(result)-i==abs(result[i]-p):
            return True
    return False

dfs(0)
print(cnt)





