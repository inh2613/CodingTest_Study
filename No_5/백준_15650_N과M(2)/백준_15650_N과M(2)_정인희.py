n,m=map(int,input().split())

lst=[]

visited=[False]*(n+1)

def dfs(start,depth):
    if depth==m:
        print(*lst)
        return
    else:
        for i in range(start,n+1):
            if visited[i]==False:
                visited[i]=True
                lst.append(i)
                dfs(start+1,depth+1)
                visited[i]=False
                start=lst.pop()

dfs(1,0)

