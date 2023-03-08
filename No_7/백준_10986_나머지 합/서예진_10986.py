# 나머지 합
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

# 가능한 나머지 수(m) 크기만큼 배열 선언
remain = [0] * m   # 누적 합을 m으로 나눴을 때의 나머지별로 카운팅
# 왜냐하면 두 누적 합을 m으로 나눴을 때의 나머지가 같다면 그 구간 합을 m으로 나눴을 때 나머지가 0이 됨

# prefix_sum = [0]
sum_value = 0
for num in num_list:
    sum_value += num
    # prefix_sum.append(sum_value)
    remain[sum_value % m] += 1

'''
시간 초과 O(N^2)
cnt = 0
for i in range(n):
    for j in range(i, n):
        total = prefix_sum[j+1] - prefix_sum[i]
        if total % m == 0:
            cnt += 1
'''

# cnt를 0번 인덱스 값으로 초기화
cnt = remain[0]
# 왜냐하면 누적합이 m으로 나누어 떨어진다면 그 자체만으로도 나누어 떨어지는 구간합이 됨

# 같은 나머지를 가진 누적 합을 2개씩 조합해서 구간 합을 구하는 경우의 수
for r in remain:
    cnt += r * (r-1) // 2

print(cnt)

'''
이렇게 풀면 .. 놀랍게도 O(n+m)이 된다네 ~
'''