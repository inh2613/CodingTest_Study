# 별 찍기 - 10
def star(num):
    if num == 1:
        return ['*']
    stars = star(num//3)
    star_list = []
    for s in stars:
        star_list.append(s*3)  # 위
    for s in stars:
        star_list.append(s + ' '*(num//3) + s)  # 가운데
    for s in stars:
        star_list.append(s*3)  # 아래
    return star_list


n = int(input())
print('\n'.join(star(n)))

