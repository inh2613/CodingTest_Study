# 신나는 함수 실행
import sys
input = sys.stdin.readline

d = {}
def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if (a, b, c) in d:
        return d[(a, b, c)]

    if a>20 or b>20 or c>20:
        return w(20, 20, 20)

    if a < b and b < c:
        d[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    d[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return d[(a, b, c)]


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    res = 'w(' + str(a) + ', ' + str(b) + ', ' + str(c) + ') = '
    res += str(w(a, b, c))
    print(res)

