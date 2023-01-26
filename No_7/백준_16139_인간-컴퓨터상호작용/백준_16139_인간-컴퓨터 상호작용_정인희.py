import sys
s=sys.stdin.readline()

q=int(sys.stdin.readline())

def solve(a,l,r):
    result = [[0] * 26 for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(26):
            if ord(s[i])-97==j:
                result[i][j]=result[i-1][j]+1
            else:
                result[i][j]=result[i-1][j]

    if l==0:
        print(result[r][ord(a)-97])
    else:
        print(result[r][ord(a)-97]-result[l-1][ord(a)-97])

for _ in range(q):
    a,l,r=sys.stdin.readline().split()
    l=int(l)
    r=int(r)
    solve(a,l,r)