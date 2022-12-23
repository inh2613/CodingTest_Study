import sys

def hanoi(n, start, temp, des, i, ans):
    if n == 0: return
    else:
        hanoi(n-1, start, des, temp, i+1, ans)
        ans.append([start, des])
        ans[0] += 1
        hanoi(n-1, temp, start, des, i+1, ans)

N = int(sys.stdin.readline())
A = [0]
hanoi(N, 1, 2, 3, 1, A)
print(A[0])
for i in range(1, len(A)):
    print(A[i][0], A[i][1])