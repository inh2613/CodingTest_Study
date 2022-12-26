# 스타트와 링크
import sys
input = sys.stdin.readline


def BT():
    global min_gap, team
    if len(start) == n // 2:
        # print(' '.join(map(str, start)))
        link = team - start
        start_list = list(start)
        sum_start, sum_link = 0, 0
        link_list = list(link)
        '''
        이렇게 능력치를 구한 것이 시간초과의 원인! 
        아래처럼 ij 능력치와 ji능력치를 한꺼번에 더해주면 반복 횟수를 줄일 수 있음
        for i in start_list:
            for j in start_list:
                if i == j:
                    continue
                sum_start += power[i][j]
        '''
        for i in range(n//2):
            for j in range(i+1, n//2):
                sum_start += power[start_list[i]][start_list[j]]
                sum_start += power[start_list[j]][start_list[i]]
        for i in range(n//2):
            for j in range(i+1, n//2):
                sum_link += power[link_list[i]][link_list[j]]
                sum_link += power[link_list[j]][link_list[i]]

        gap = abs(sum_start - sum_link)
        if gap < min_gap:
            min_gap = gap
        return

    for i in range(n):
        if i in start:
            continue
        ls = list(start)
        if len(ls) > 0 and ls[-1] > i:
            continue
        start.add(i)
        BT()
        start.remove(i)


n = int(input())
power = []
for _ in range(n):
    power.append(list(map(int, input().split())))

team = set()
team.update([i for i in range(n)])

start = set()
min_gap = 1e9

BT()
print(min_gap)