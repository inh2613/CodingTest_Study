#진짜 이건 이해 못함

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        a,b,c=0,0,0

        cnt[a][b][c]=1



    elif a>20 or b>20 or c>20:
        a,b,c,=20,20,20
        if cnt[a][b][c] == 0:
            cnt[a][b][c]=w(20,20,20)



    elif a<b and b<c:
        if cnt[a][b][c] == 0:
            cnt[a][b][c]= w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)


    else:
        if cnt[a][b][c] == 0:
            cnt[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


    return cnt[a][b][c]

global cnt

cnt = [[[0] * 51 for _ in range(51)] for _ in range(51)]

while True:

    a,b,c=map(int,input().split())


    if a==-1 and b==-1 and c==-1:
        break

    answer=w(a,b,c)

    print('w(%d, %d, %d) = %d' %(a,b,c,answer))


