# 스택 수열
n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

end = 0
res = ''
stack = []
for i in range(n):
    if end < seq[i]:
        res += '+' * (seq[i] - end)
        res += '-'
        for j in range(end+1, seq[i]+1):
            stack.append(j)
        stack.pop()

        end = seq[i]
    elif end > seq[i]:
        if stack[-1] != seq[i]:
            res = ''
            break
        else:
            res += '-'
            stack.pop()

if res == '':
    print('NO')
else:
    for r in res:
        print(r)
