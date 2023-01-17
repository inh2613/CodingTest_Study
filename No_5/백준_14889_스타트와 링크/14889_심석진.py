import sys

N = int(sys.stdin.readline())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
teamS = []
teamL = []
ans = sys.maxsize


def bt(n):
    global ans
    Sstat = 0
    Lstat = 0
    if len(teamS) == N//2:
        for i in range(N):
            if i in teamS: continue
            teamL.append(i)

        for i in range(N//2):
            for j in range(N//2):
                Sstat += stat[teamS[i]][teamS[j]]
                Lstat += stat[teamL[i]][teamL[j]]

        tmp = abs(Sstat - Lstat)
        ans = min(ans, tmp)

        teamL.clear()
        return

    for i in range(n, N):
        teamS.append(i)
        bt(i+1)
        teamS.pop()


bt(0)
print(ans)