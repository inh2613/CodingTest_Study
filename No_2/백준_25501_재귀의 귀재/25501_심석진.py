import sys

def recursion(s, l, r, i):
    if l >= r: return [1, i]
    elif s[l] != s[r]: return [0, i]
    else:
        i += 1
        return recursion(s, l+1, r-1, i)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

N = int(sys.stdin.readline())
for _ in range(N):
    S = sys.stdin.readline().strip()
    ans = isPalindrome(S)
    print(ans[0], ans[1])