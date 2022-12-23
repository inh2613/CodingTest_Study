def star(n):
    if n == 3: return ['***', '* *', '***']

    stars = star(n//3)
    ans = []

    for s in stars:
        ans.append(s*3)

    for s in stars:
        ans.append(s + ' '*(n//3) + s)

    for s in stars:
        ans.append(s*3)

    return ans

N = int(input())
print('\n'.join(star(N)))


'''
def star(row, col, num):
    if (row//(num/3))%3 == 1 and (col//(num/3))%3 == 1:
        print(' ', end='')

    else:
        if num == 3: print('*', end='')
        else: star(row, col, num/3)


N = int(input())
for i in range(N):
    for j in range(N):
        star(i,j,N)
    print()
'''