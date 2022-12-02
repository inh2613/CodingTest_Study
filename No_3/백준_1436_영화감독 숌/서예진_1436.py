# 영화감독 숌

n = int(input())

num = 666
cnt = 0
while cnt < n:
    if str(num).find('666') != -1:
        cnt += 1
    num += 1

print(num-1)