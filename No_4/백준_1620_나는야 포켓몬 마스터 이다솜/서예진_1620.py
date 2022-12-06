import sys
input = sys.stdin.readline

n, m = map(int, input().split())
monster = {}
monster_name_key = {}
for i in range(n):
    case = input().rstrip()
    monster[i+1] = case
    monster_name_key[case] = i+1

for i in range(m):
    s = input().rstrip()

    if s.isnumeric():
        print(monster[int(s)])
    else:
        print(monster_name_key[s])




