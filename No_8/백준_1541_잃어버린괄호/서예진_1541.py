# 잃어버린 괄호
eq = list(input())

# 식의 값이 최소가 되려면 -를 기준으로 -가 다시 나올 때까지 괄호로 묶기
l = len(eq)
for i in range(l):
    if eq[i] == '-':
        for j in range(i+1, l):
            if eq[j] == '+':
                eq[j] = '-'
            elif eq[j] == '-':
                break

num = []
operator = []
eq = ''.join(eq)

idx = -1
# 첫번째 부호 찾기
for i in range(l):
    if eq[i] == '+' or eq[i] == '-':
        idx = i
        operator.append(eq[i])
        break

if idx != -1:
    num.append(eq[0:idx])
    idx += 1
    start = idx
    while True:
        if idx == l - 1:
            num.append(eq[start:l])
            break
        if eq[idx] == '+' or eq[idx] == '-':
            operator.append(eq[idx])
            num.append(eq[start:idx])
            idx += 1
            start = idx
        else:
            idx += 1
else:
    num.append(eq)

n = len(num)
for i in range(n):
    num[i] = num[i].lstrip('0')
    if num[i] == '':
        num[i] = '0'

# 수와 연산자 합치기
res = ''
for i in range(n-1):
    res += num[i] + operator[i]
res += num[n-1]

print(eval(res))
