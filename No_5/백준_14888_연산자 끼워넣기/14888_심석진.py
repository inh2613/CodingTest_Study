import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
opN = list(map(int, sys.stdin.readline().split()))
op = []

M = -1000000000
m = 1000000000


def cal(num1, num2, operator):
    if operator == 0: return num1+num2
    if operator == 1: return num1-num2
    if operator == 2: return num1*num2
    if operator == 3:
        if num1 < 0:
            num1 *= -1
            return num1 // num2 * -1
        else: return num1//num2


def dfs():
    global M, m
    if len(op) == N-1:
        ans = A[0]
        for j in range(N-1): ans = cal(ans, A[j+1], op[j])

        if ans > M: M = ans
        if ans < m: m = ans
        return

    for i in range(4):
        if opN[i] == 0: continue
        op.append(i)
        opN[i] -= 1
        dfs()
        op.pop()
        opN[i] += 1


dfs()
print(str(M) + '\n' + str(m))

'''
n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split());
max_result = - int(1e9)
min_result = int(1e9)

def dfs(sum, idx):
    global max_result, min_result, add, sub, mul, div
    
    if idx == n:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return
    
    if add :    # 0은 if문에서 False 취급. add != 0과 동일
        add -= 1
        dfs(sum + number[idx], idx + 1)
        add += 1
    if sub :
        sub -= 1
        dfs(sum - number[idx], idx + 1)
        sub += 1
    if mul :
        mul -= 1
        dfs(sum * number[idx], idx + 1)
        mul += 1
    if div :
        div -= 1
        dfs(int(sum / number[idx]), idx + 1)
        div += 1
        
dfs(number[0], 1)

print(max_result)
print(min_result)
'''