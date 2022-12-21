n,m=map(int,input().split())
visited=[False]*n
lst=[]

def dfs(depth):
    if depth==m:
        #print(' '.join(map(str,lst)))
        print(*lst)
        return
    else:
        for i in range(n):
            if visited[i]==False:
                visited[i]=True
                lst.append(i+1)
                dfs(depth+1)
                visited[i]=False
                lst.pop()


dfs(0)