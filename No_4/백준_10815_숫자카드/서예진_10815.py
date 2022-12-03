# 숫자 카드
import sys
input = sys.stdin.readline


def binary_search(ar, target):
    start = 0
    end = len(ar)-1
    while start <= end:
        mid = (start + end) // 2
        if ar[mid] == target:
            return mid
        elif ar[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
m = int(input())
check_list = list(map(int, input().split()))

for num in check_list:
    res = binary_search(num_list, num)
    if res is None:
        print(0, end=' ')
    else:
        print(1, end=' ')



