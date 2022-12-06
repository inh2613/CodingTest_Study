# 숫자 카드 2
# 계수 정렬을 이용한 풀이
'''
import sys
input = sys.stdin.readline

n = int(input())
count_cards = [0] * 20000001
cards = list(map(int, input().split()))

for num in cards:
    count_cards[num] += 1

m = int(input())
c_list = list(map(int, input().split()))
for card in c_list:
    print(count_cards[card], end=' ')

'''
''''''''''이진탐색을 이용한 풀이'''''''''''''''
'''
import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
num_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


dic = {}
for card in cards:
    if card not in dic:
        dic[card] = binary_search(cards, card, 0, n-1)

print(' '.join(str(dic[x]) if x in dic else '0' for x in num_list ))

'''

# 해싱을 이용한 풀이
# 해쉬 자료구조는 주로 딕셔너리로 구현
import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))

m = int(input())
num_list = list(map(int, input().split()))

hashmap = {}
for card in cards:
    if card in hashmap:
        hashmap[card] += 1
    else:
        hashmap[card] = 1

print(' '.join(str(hashmap[x]) if x in hashmap else '0' for x in num_list))
