n = int(input())

visited = [False]*(n) #1차원배열
#print(visited)
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)
l = []

def dfs(start,depth):

    global min_diff
    if depth==n//2:
        power_start,power_link=0,0
        for i in range(n):
            for j in range(n):
                if visited[i]==True and visited[j]==True:
                    power_start+=graph[i][j]
                elif visited[i]==False and visited[j]==False:
                    power_link+=graph[i][j]

        min_diff=min(min_diff,abs(power_start-power_link))

        return

    else:
        for i in range(start,n):
            if visited[i]==False:
                visited[i]=True
                l.append(i)
                dfs(start+1,depth+1)

                visited[i]=False
                start=l.pop()



dfs(1,0)

print(min_diff)