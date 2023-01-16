import sys

N = int(sys.stdin.readline())
N_num = list(map(int, sys.stdin.readline().split()))
N_num.sort()
#N_num = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_num = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, start, end):
    if start > end:
        print(0, end=' ')
        return

    mid = (start+end) // 2
    if arr[mid] == target: print(1, end=' ')
    elif arr[mid] > target: binary_search(arr, target, start, mid-1)
    else: binary_search(arr, target, mid+1, end)


for i in range(M):
    binary_search(N_num, M_num[i], 0, N-1)

'''
for i in M_num:
    if i in N_num: print(1, end=' ')
    else: print(0, end=' ')
'''