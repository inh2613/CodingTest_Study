# 분해합

def is_generator(num):
    res = num
    while num > 0:
        res += num % 10
        num = num // 10
    return res


n = int(input())
result = 0
for num in range(1, n):
    if is_generator(num) == n:
        result = num
        break

print(result)
