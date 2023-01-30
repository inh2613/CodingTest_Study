n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr_1=[[0]*n for _ in range(n)] # 가로 누적합
arr_2=[[0]*n for _ in range(n)] # 세로 누적합

for i in range(n):
    arr_1[i][0]=arr[i][0]
    arr_2[0][i]=arr[0][i]

for i in range(n):
    for j in range(1,n):
        arr_1[i][j]=arr_1[i][j-1]+arr[i][j]
for i in range(1,n):
    for j in range(n):
        arr_2[i][j]=arr_2[i-1][j]+arr[i][j]

def solve(x1,y1,x2,y2):
    _sum1,_sum2,_sum3=0,0,0
    if x1==x2 and y1==y2:
        return arr[x1][y1]

    for i in range(x2+1):
        _sum1+=arr_1[i][y2]
    # print('_sum1', _sum1)

    if x1>0 and y1>0:
        for i in range(y2-y1+1):
            _sum2+=arr_2[x2][i]
        for i in range(x2-x1+1):
            _sum2+=arr_1[i][y2]
        # print(_sum2)

        for i in range(x1):
            _sum3 += arr_1[i][y1-1]

        return _sum1 - _sum2 + _sum3

    elif x1 == 0 and y1 == 0:
        return _sum1

    elif x1==0 and y1!=0:
        for i in range(y2-y1+1):
            _sum2+=arr_2[x2][i]
            # print(_sum2)
        return _sum1-_sum2

    elif x1!=0 and y1==0:
        for i in range(x2-x1+1):
            _sum2+=arr_1[i][y2]
            # print(_sum2)
        return _sum1 - _sum2


for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    answer=solve(x1-1,y1-1,x2-1,y2-1)
    # print('answer',answer)
    # print('------------')
    print(answer)
