def merge(A, p, q, r, num):
    i = p
    j = q+1
    t = 0
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
        t += 1

    while i <= q:
        tmp.append(A[i])
        t += 1
        i += 1

    while j <= r:
        tmp.append(A[j])
        t += 1
        j += 1

    i = p
    t = 0
    global cnt, tf
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == num:
            tf = A[i]
            return
        i += 1
        t += 1

def merge_sort(A, p, r, num):
    if p < r and cnt <= num:
        q = (p+r) // 2
        merge_sort(A, p, q, num)
        merge_sort(A, q+1, r, num)
        merge(A, p, q, r, num)


N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
tf = -1
merge_sort(A, 0, N-1, K)
print(tf)
print(A)