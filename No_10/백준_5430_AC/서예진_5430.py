# AC
from collections import deque
import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    funcs = list(input().rstrip('\n'))
    n = int(input())
    num_string = input().rstrip('\n')
    num_string = num_string[1:-1]
    if num_string == '':
        num_list = deque()
    else:
        num_list = deque(map(int, num_string.split(',')))

    # True는 앞, False는 뒤
    check = True
    error = False

    for func in funcs:
        if func == 'R':
            check = not check
        else:
            if len(num_list) == 0:
                error = True
                continue
            else:
                if check:
                    num_list.popleft()
                else:
                    num_list.pop()

    if error:
        print('error')
    else:
        l = len(num_list)
        if l == 0:
            res = '[]'
        else:
            res = '['
            if check:
                for i in range(l):
                    res += str(num_list[i])
                    res += ','
                res = res[:-1]
                res += ']'
            else:
                for i in range(l - 1, -1, -1):
                    res += str(num_list[i])
                    res += ','
                res = res[:-1]
                res += ']'
        print(res)
