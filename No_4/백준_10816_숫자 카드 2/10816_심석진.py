import sys

N = int(sys.stdin.readline())
N_num = list(map(int, sys.stdin.readline().split()))
N_num.sort()
N_count = {}
for num in N_num:
    if num in N_count: N_count[num] += 1
    else: N_count[num] = 1

M = int(sys.stdin.readline())
M_num = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, start, end):
    if start > end:
        print(0, end=' ')
        return

    mid = (start+end) // 2
    if arr[mid] == target: print(N_count[target], end=' ')

    elif arr[mid] > target: binary_search(arr, target, start, mid-1)
    else: binary_search(arr, target, mid+1, end)


for i in M_num: binary_search(N_num, i, 0, N-1)
'''
for num in M_num:
    if num in N_count: print(N_count[num], end=' ')
    else: print(0, end=' ')
'''