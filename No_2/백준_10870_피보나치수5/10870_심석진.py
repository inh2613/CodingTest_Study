def fivo(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        ans = fivo(n-2) + fivo(n-1)
        return ans

N = int(input())
print(fivo(N))