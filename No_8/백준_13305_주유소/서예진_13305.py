# 주유소
n = int(input())
d = list(map(int, input().split()))
price = list(map(int, input().split()))

total_price = d[0] * price[0]
lower_price = price[0]
d_sum = 0

for i in range(1, n-1):
    if lower_price > price[i]:
        total_price += lower_price * d_sum
        lower_price = price[i]
        d_sum = d[i]
    else:
        d_sum += d[i]

total_price += lower_price * d_sum
print(total_price)
