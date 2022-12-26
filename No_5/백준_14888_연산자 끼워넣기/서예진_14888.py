# 연산자 끼워넣기
n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))

oper = dict()
oper['+'] = oper_list[0]
oper['-'] = oper_list[1]
oper['*'] = oper_list[2]
oper['//'] = oper_list[3]

oper_arr = ['+', '-', '*', '//']

seq = []
mini = 10 ** 9
maxi = -1 * 10 ** 9


def BT():
    global maxi
    global mini
    if len(seq) == n-1:
        # print(' '.join(map(str, seq)))
        if seq[0] == '//' and num_list[0] < 0:
            tmp = str(num_list[0] * (-1)) + seq[0] + str(num_list[1])
            res = eval(tmp) * (-1)
        else:
            tmp = str(num_list[0]) + seq[0] + str(num_list[1])
            res = eval(tmp)

        for i in range(1, n-1):
            if seq[i] == '//' and res < 0:
                tmp = str(res * (-1)) + seq[i] + str(num_list[i+1])
                res = eval(tmp) * (-1)
            else:
                tmp = str(res) + seq[i] + str(num_list[i+1])
                res = eval(tmp)
        if res > maxi:
            maxi = res
        if res < mini:
            mini = res
        return

    for i in range(4):
        if oper[oper_arr[i]] <= 0:
            continue
        seq.append(oper_arr[i])
        oper[oper_arr[i]] -= 1
        BT()
        seq.pop()
        oper[oper_arr[i]] += 1


BT()
print(maxi)
print(mini)


