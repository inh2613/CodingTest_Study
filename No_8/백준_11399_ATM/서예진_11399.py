# ATM
n = int(input())
time = list(map(int, input().split()))

# 시간이 적게 걸리는 사람부터 앞에 서야
# 모든 사람이 기다리는 시간이 최소
time.sort()

for i in range(1, n):
    time[i] = time[i-1] + time[i]

print(sum(time))
