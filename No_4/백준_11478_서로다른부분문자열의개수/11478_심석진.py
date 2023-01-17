import sys

S = sys.stdin.readline()
ans = set()

for i in range(len(S)):
    for j in range(1, len(S)-i):
        ans.add(S[i:i+j])

print(len(ans))