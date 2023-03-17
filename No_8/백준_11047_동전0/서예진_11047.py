# 동전 0
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

total = 0
while coins:
    coin = coins.pop()
    cnt = k // coin
    total += cnt
    k -= cnt * coin

print(total)

# 동전의 가치가 배수이기 때문에 그리디 가능