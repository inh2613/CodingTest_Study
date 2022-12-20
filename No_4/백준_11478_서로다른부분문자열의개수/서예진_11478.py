# 서로 다른 부분 문자열의 개수
s = input()
l = len(s)
sub_string = set()
for i in range(l):
    for j in range(i+1, i+l+1):
        if j > l:
            continue
        sub_string.add(s[i:j])

print(len(sub_string))

'''
문자열의 길이(N) : 10^3 이하
O(N^2) = O(10^6)
문자열 슬라이싱 s[start:end:step] : 인덱스 start부터 "end-1"까지!
'''