def print_star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        arr = print_star(n // 3)

        star = []

        for i in arr:
            star.append(i * 3)
        for i in arr:
            star.append(i + " " * (n // 3) + i)
        for i in arr:
            star.append(i * 3)

        return star


n = int(input())

star = print_star(n)

# print(star)

for i in range(n):
    print(star[i])